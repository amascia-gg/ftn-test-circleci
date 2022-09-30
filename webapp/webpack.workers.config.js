const path = require('path');
const webpack = require('webpack');

module.exports = (env) => ({
  entry: './workers/_worker.js',
  devtool: 'source-map',
  mode: 'production',
  output: {
    path: path.resolve(__dirname, './workers/out'),
    filename: '_worker-bundle.js',
    library: {
      type: 'module',
    },
  },
  experiments: {
    outputModule: true,
  },
  plugins: [
    new webpack.DefinePlugin({
      'process.env.SENTRY_RELEASE': JSON.stringify(env.SENTRY_RELEASE),
    }),
  ],
});
