// Enhanced data processing functionality
function processData(input) {
    // Validate input
    if (!input || typeof input !== 'object') {
        throw new Error('Invalid input data');
    }
    
    // Process data with improved algorithm
    const processed = Object.keys(input).map(key => ({
        key,
        value: input[key],
        timestamp: Date.now(),
        processed: true
    }));
    
    return processed;
}