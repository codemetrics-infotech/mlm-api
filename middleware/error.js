const ErrorResponse = require('../utils/errorResponse')

const errorHandler =  (err, req, res, next) => {
    console.log(err);
    let error = { ...err }

    // console.log(err.stack.red)
    console.log(err.message)

    error.message = err.message;
    console.log(error.message)

    // Mongoose bad Object
    if (err.name === 'CastError') {
        const message = `Employee not found with id ${err.value}`;
        error = new ErrorResponse(message, 404);
    };
    
    // Mongoose Duplicate key
    if (err.code === 11000) {
        const message = `Duplicate fields value entered`;
        error = new ErrorResponse(message, 400);
    };

    // Mongoose Validaore Error
    if (err.name === 'ValidationError') {
        console.log('Error in Validation......', err.name)
        const message = Object.values(err.errors).map(val => val.message);
        console.log(message)
        error = new ErrorResponse(message, 400);
    };

    res.status(error.statusCode || 500).json({
        success: false,
        error: error.message || 'Server Error'
    });
};

module.exports = errorHandler;