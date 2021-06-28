function snakeToCamel(word) {
    const arr = word.split('_');
    for (let i = 1; i < arr.length; i++) {
        const capitalized = arr[i].charAt(0).toUpperCase() + arr[i].slice(1);
        arr[i] = capitalized;
    }
    return arr.join('');
}
