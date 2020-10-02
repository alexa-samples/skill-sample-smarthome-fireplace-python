const path = require('path')

module.exports = {
  entry: {
    app: ['./src/fireplace.js']
  },
  mode: 'development', 
  output: {
    path: path.resolve(__dirname, 'public'),
    filename: '[name].js',
  },
  devServer: {
    publicPath: '/public/',
    compress: true,
    port: 9000
  }
}
