import Document, { Html, Head, Main, NextScript } from 'next/document';
import React from 'react';
import createEmotionServer from '@emotion/server/create-instance';
import createEmotionCache from '../mui/createEmotionCache';
import theme from '../mui/theme';

export default class MyDocument extends Document {
  render() {
    return (
      <Html lang="en">
        <Head>
          <noscript>
            <meta httpEquiv="refresh" content="0; url=./nojs" />
          </noscript>
          <meta name="theme-color" content={theme.palette.primary.main} />
          <link rel="manifest" href="/manifest.webmanifest" />
          <link rel="icon" href="/icons/favicon.ico" sizes="any" />
          <link rel="icon" type="image/svg+xml" href="/icons/square-flag.svg" />
          <link rel="apple-touch-icon" href="./icons/apple-touch-icon.png" />
          <link rel="preconnect" href="https://fonts.googleapis.com" />
          <link
            rel="stylesheet"
            href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
          />
          <link
            rel="preload"
            as="image"
            href="../public/images/unionjack-extra-small.webp"
            type="image/webp"
          />

          <meta name="emotion-insertion-point" content="" />
          {this.props.emotionStyleTags}
        </Head>
        <body>
          <Main />
          <NextScript />
        </body>
      </Html>
    );
  }
}

MyDocument.getInitialProps = async (ctx) => {
  // Resolution order
  //
  // On the server:
  // 1. app.getInitialProps
  // 2. page.getInitialProps
  // 3. document.getInitialProps
  // 4. app.render
  // 5. page.render
  // 6. document.render
  //
  // On the server with error:
  // 1. document.getInitialProps
  // 2. app.render
  // 3. page.render
  // 4. document.render
  //
  // On the client
  // 1. app.getInitialProps
  // 2. page.getInitialProps
  // 3. app.render
  // 4. page.render

  const originalRenderPage = ctx.renderPage;

  // You can consider sharing the same Emotion cache between all the SSR requests to speed up performance.
  // However, be aware that it can have global side effects.
  const cache = createEmotionCache();
  const { extractCriticalToChunks } = createEmotionServer(cache);

  ctx.renderPage = () =>
    originalRenderPage({
      enhanceApp: (App) =>
        function EnhanceApp(props) {
          // eslint-disable-next-line react/jsx-props-no-spreading
          return <App emotionCache={cache} {...props} />;
        },
    });

  const initialProps = await Document.getInitialProps(ctx);
  // This is important. It prevents Emotion to render invalid HTML.
  // See https://github.com/mui/material-ui/issues/26561#issuecomment-855286153
  const emotionStyles = extractCriticalToChunks(initialProps.html);
  const emotionStyleTags = emotionStyles.styles.map((style) => (
    <style
      data-emotion={`${style.key} ${style.ids.join(' ')}`}
      key={style.key}
      // eslint-disable-next-line react/no-danger
      dangerouslySetInnerHTML={{ __html: style.css }}
    />
  ));

  return {
    ...initialProps,
    emotionStyleTags,
  };
};
