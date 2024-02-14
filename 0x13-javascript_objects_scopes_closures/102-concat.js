#!/usr/bin/node

const fs = require('fs');

// Check if the correct number of command line arguments is provided
if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

const fileAPath = process.argv[2];
const fileBPath = process.argv[3];
const fileCPath = process.argv[4];

const fileAContent = fs.readFileSync(fileAPath, 'utf-8');
const fileBContent = fs.readFileSync(fileBPath, 'utf-8');

const concatenatedContent = fileAContent + '\n' + fileBContent;

fs.writeFileSync(fileCPath, concatenatedContent);
