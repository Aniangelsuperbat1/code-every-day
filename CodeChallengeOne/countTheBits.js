// Write a function called countTheBits that accepts a single numeric argument that will be an integer.

// The function should return the number of bits set to 1 in the number's binary representation.

const countTheBits = (num) => {
  return num
    .toString(2)
    .split("")
    .filter((num) => num === "1").length;
};

console.log(countTheBits(13));
