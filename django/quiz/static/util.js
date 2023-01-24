function formatTime(time) {
    let date = new Date(time);

    const options = {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
    };
    return date.toLocaleString('en-US', options);
}
