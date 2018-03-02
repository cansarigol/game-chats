var path = require('path')
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
    context: __dirname,
    entry: {
        
    },
    output: {
        path: path.resolve('./assets/bundles/'), 
        filename: '[name]-[hash].js', 
    },
    
    plugins: [
        new webpack.ProvidePlugin({ 
            $: 'jquery',
            jQuery: 'jquery',
            'window.jQuery': 'jquery' 
        })
    ],
    
    module: {
        loaders: [
            {test: /\.jsx?$/, 
                exclude: /node_modules/,
                loaders: ['react-hot', 'babel'], 
            }
        ]
    },
    
    resolve: {
        modulesDirectories: ['node_modules'],
        extensions: ['', '.js', '.jsx'] 
    }   
}