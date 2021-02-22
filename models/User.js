const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');

const UserSchema = new mongoose.Schema({
    firstName: {
        type: String,
        required: [true, 'Please add first name']
    },
    middleName: {
        type: String,
    },
    lastName: {
        type: String,
        required: [true, 'Please add last name']
    },
    fatherName: {
        type: String,
        required: [true, 'Please add father name']
    },
    maritalStatus: {
        type: String,
        required: [true, 'Please add merital status']
    },
    email: {
        type: String,
        required: [true, 'Please add email'],
        unique: true,
        trim: true,
        maxlength: [50, 'Email con not be more then 50 characters'],
        match: [/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/, 'Please provide valid email']
    },
    birthDate: {
        type: Date
    },
    panCard: {
        type: String,
        required: [true, 'Please add pan card']
    },
    gender: {
        type: String,
        required: [true, 'Please add gender']
    },
    mobileNumber: {
        type: Number,
        required: [true, 'Please add mobile number'],
        min: 10
    },
    password: {
        type: String,
        required: [true, 'Please add password'],
        minlength: [8, 'Password can not less then 8 cherectores'],
        select: false
    },
    role: {
        type: String,
        enum: ['isAdmin', 'isMenter', 'isUser'],
        default: 'isUser'
    },
    lastLogin: {
        type: Date
    },
    resetPasswordToken: String,
    resetPasswordExpire: Date,
    joinedDate: {
        type: Date,
        default: Date.now
    },
});

// Encrept password using bcrypt
UserSchema.pre('save', async function(next) {
    const salt = await bcrypt.genSalt(10);
    this.password = await bcrypt.hash(this.password, salt);
});

// Validate Password & Retuen
UserSchema.methods.matchPassword = async function(enteredPassword) {
    return await bcrypt.compare(enteredPassword, this.password);
};

module.exports = mongoose.model('User', UserSchema);