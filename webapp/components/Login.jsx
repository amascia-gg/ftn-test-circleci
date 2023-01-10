import React, { useEffect, useState, useCallback } from 'react';
import SvgIcon from '@mui/material/SvgIcon';
import Button from '@mui/material/Button';
import { nanoid } from 'nanoid';
import { useRouter } from 'next/router';

export default function Login() {
  const [client, setClient] = useState(null);
  const [loggedIn, setLoggedIn] = useState(false);
  const router = useRouter();

  const onload = () => {
    const GOOGLE_CLIENT_ID =
      '263846603498-57v6mk1hacurssur6atn1tiplsnv4j18.apps.googleusercontent.com';

    window.google.accounts.id.initialize({
      client_id: GOOGLE_CLIENT_ID,
      callback: (response) => {
        if (!response.credential || !response.clientId) {
          throw new Error('Failed to initialize google sign in');
        }
      },
    });

    const state = nanoid();
    sessionStorage.setItem('state', state);

    const clientRef = window.google.accounts.oauth2.initCodeClient({
      client_id: GOOGLE_CLIENT_ID,
      scope: 'openid profile email',
      ux_mode: 'redirect',
      state,
      redirect_uri:
        process.env.NODE_ENV === 'development'
          ? 'http://localhost:8787/auth'
          : 'https://bemstudios.uk/auth',
      callback: (response) => {
        if (response.error) {
          throw new Error('Failed to initCodeClient', response.error);
        }
      },
    });

    setClient(clientRef);
    clientRef.requestCode();
  };

  const onClick = useCallback(() => {
    if (loggedIn) {
      router.push('/home');
      return;
    }
    if (client) {
      client.requestCode();
      return;
    }

    const script = document.createElement('script');

    script.src = 'https://accounts.google.com/gsi/client';
    script.onload = onload;
    script.onerror = () => {
      throw new Error('Google gsi script failed to load');
    };

    document.body.appendChild(script);
  }, [loggedIn, router, client]);

  useEffect(() => {
    const match = document.cookie.match(/(^| )auth=([^;]+)/);
    const hasValidAuth = match !== null && match[2] !== 'deleted';
    setLoggedIn(hasValidAuth);
  }, []);

  return (
    <Button
      variant="contained"
      color="primary"
      size="large"
      startIcon={
        <SvgIcon>
          <path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z" />
        </SvgIcon>
      }
      onClick={onClick}
    >
      {loggedIn ? 'Home' : 'Login'}
    </Button>
  );
}
