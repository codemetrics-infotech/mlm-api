const User = require('../models/User');
const asyncHandler = require('../middleware/async');
const ErrorResponse = require('../utils/errorResponse');

// @desc        Register User
// @route       POST /api/v1/user/register
// @access      Pyblic
exports.registerUser = asyncHandler(async (req, res, next) => {
    const {
        firstName,
        middleName,
        lastName,
        fatherName,
        maritalStatus,
        email,
        panCard,
        gender,
        mobileNumber,
        password,
        role
    } = req.body;

    const user = await User.create({
        firstName,
        middleName,
        lastName,
        fatherName,
        maritalStatus,
        email,
        panCard,
        gender,
        mobileNumber,
        password,
        role
    });

    res.status(200).json({
        success: true,
        data: user
    });
});

// @desc        Login User
// @route       POST /api/v1/user/login
// @access      Pyblic
exports.loginUser = asyncHandler(async (req, res, next) => {
    const { email, password } = req.body;

    // Validate email & password
    if(!email || !password ) {
        return next(new ErrorResponse(`Please provade valid email & password`, 400));
    };

    // Chech for user
    const user = await User.findOne({ email }).select('+password');

    if(!user) {
        return next(new ErrorResponse(`Invalide credentials`, 401));
    };

    // Validate password
    const isPassword = await user.matchPassword(password);

    if(!isPassword) {
        return next(new ErrorResponse(`Invalide credentials`, 401));
    };

    res.status(200).json({
        success: true,
        data: user
    });
});