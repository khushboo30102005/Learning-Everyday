try {
  const data = require('./data.json');
  // console.log(data);
  // console.log(typeof data);
  // const name = data.name
  // console.log(name);
  // console.log(data.marks[0]);
  // console.log(data.score[0].f2);
  // console.log(Object.keys(data));
  // console.log(Object.values(data));
  for (key in data) {
    if (typeof data[key] !== 'object') {
      console.log(`${key}->  ${data[key]}`);
    } else if (data[key] instanceof Array) {
      const arr = data[key];
      if (typeof arr[0] !== 'object') {
        for (e of arr) {
          console.log(e);
        }
      } else {
        for (e of arr) {
          for (k1 in e) {
            console.log(`${k1} ->  ${e[k1]}`);
          }
        }
      }
    } else {
      for (k in data[key]) {
        console.log(`${k} ->  ${data[key][k]}`);
      }
    }
  }
} catch (error) {
  console.log(error);
}
