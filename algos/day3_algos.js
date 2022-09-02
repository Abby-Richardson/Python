function encodeStr(str) {
    let encoded = "";

    for (let i = 0; i < str.length; i++) {
        let currChar = str[i];
        let dupeCount = 1;

        while (str[i + 1] === currChar) {
            dupeCount++;
            i++;
        }

        if (dupeCount === 1) {
            encoded += currChar
        }
        else if (dupeCount === 2) {
            encoded += currChar + currChar
        }
        else {
            encoded += currChar + dupeCount;
        }
    }
    return encoded;
}