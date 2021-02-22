const asyncHandler = fn => (req, res, next) => {
    Promise.resolve(fn(req, res, next)).catch(next);
    // console.log("I'm in async handler", Promise.resolve(fn(req, res, next)));
};

module.exports = asyncHandler;