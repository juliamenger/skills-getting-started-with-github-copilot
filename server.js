const express = require('express');
const app = express();

app.use('/static', express.static('src/static')); // Servir arquivos estáticos

app.get('/activities', (req, res) => {
  res.json({
    Soccer: {
      description: "Join the soccer team and compete in tournaments.",
      schedule: "Mondays and Wednesdays, 4-6 PM",
      max_participants: 20,
      participants: ["Alice", "Bob"]
    },
    "Chess Club": {
      description: "Learn and play chess with others.",
      schedule: "Fridays, 3-5 PM",
      max_participants: 15,
      participants: ["Charlie"]
    }
  });
});

app.listen(8000, () => {
  console.log('Server running on http://localhost:8000');
});
