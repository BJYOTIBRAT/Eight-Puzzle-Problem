// Utility functions for better error handling
const utils = {
    validateInput: (data) => {
        return data && typeof data === 'object' && Object.keys(data).length > 0;
    },
    
    formatError: (error) => {
        return {
            message: error.message,
            timestamp: new Date().toISOString(),
            stack: error.stack
        };
    },
    
    logActivity: (action, details) => {
        console.log(`[${new Date().toISOString()}] ${action}:`, details);
    }
};