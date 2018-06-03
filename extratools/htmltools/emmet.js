#! /usr/bin/env node

var emmet = require('@emmetio/expand-abbreviation');

console.log(emmet.expand(process.argv[2]));
