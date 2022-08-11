const webpack = require('webpack');
const isProd = process.env.NODE_ENV === "server";

module.exports = {
  configureWebpack: {
    // Set up all the aliases we use in our app.
    plugins: [
      new webpack.optimize.LimitChunkCountPlugin({
        maxChunks: 6
      })
    ]
  },
  chainWebpack: config => {
    config.module.rules.delete('eslint');
  },
  transpileDependencies: ['vuetify'],
  pwa: {
    themeColor: '#172b4d',
    msTileColor: '#172b4d',
    appleMobileWebAppCapable: 'yes',
    appleMobileWebAppStatusBarStyle: '#172b4d'
  },
  css: {
    // Enable CSS source maps.
    sourceMap: !isProd
  }
};
