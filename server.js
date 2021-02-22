const express = require('express');
const color = require('colors');
const dotenv = require('dotenv');
const cors = require('cors')
const helmet = require('helmet');

const errorHandler = require('./middleware/error');

const connectDB = require('./config/db');

// Load env vers
dotenv.config({ path: './config/config.env' });

// Connect database
connectDB();

// Import routers
const user = require('./routes/user');

const app = express();

app.use(express.json())

// Set security headers
app.use(helmet())

// Set CORS origin
const corsOptions = {
    origin: '*',
    optionsSuccessStatus: 200
};

// Use routes
app.use('/api/v1/user', cors(corsOptions), user);

app.use(errorHandler);

// Initialize port
const PORT = process.env.PORT || 3000;

app.listen(PORT, console.log(`Server is runing on ${process.env.NODE_ENV} mode on port ${PORT}`.bgMagenta.black));
