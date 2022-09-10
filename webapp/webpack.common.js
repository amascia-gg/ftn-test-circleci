const BundleTracker = require('webpack-bundle-tracker');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CopyPlugin = require('copy-webpack-plugin');

const path = require('path');

module.exports = (env) => ({
  context: __dirname,
  entry: './main/src/App.jsx',
  output: {
    path: path.resolve('./assets/webpack_bundles/'),
    filename: '[name]-[contenthash].js',
  },
  plugins: [
    new BundleTracker({ filename: './webpack-stats.json' }),
    new CopyPlugin({
      patterns: [
        {
          from: path.resolve('./main/src/icons/favicon.ico'),
          to: path.resolve('./assets/webpack_bundles/'),
        },
      ],
    }),
    new HtmlWebpackPlugin({
      template: './main/templates/main/index.ejs',
      title: 'British Empire Management',
      filename: 'index.html',
      templateParameters: {
        debug: env.DEBUG,
        release: process.env.CF_PAGES_COMMIT_SHA,
      },
      meta: {
        charset: 'utf-8',
        viewport: 'width=device-width, initial-scale=1',
      },
    }),
  ],
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: [
          {
            loader: 'babel-loader',
          },
        ],
      },
      {
        test: /\.(png|svg|jpg|jpeg|gif|ico)$/i,
        type: 'asset/resource',
      },
      {
        test: /\.css$/,
        use: 'css-loader',
      },
    ],
  },
  resolve: {
    extensions: ['.jsx', '...'],
  },
});
