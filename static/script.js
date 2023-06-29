document.addEventListener('DOMContentLoaded', () => {
  loadSubscriptions();

  const subscriptionForm = document.getElementById('subscriptionForm');
  subscriptionForm.addEventListener('submit', (event) => {
      event.preventDefault();
      const emailInput = document.getElementById('emailInput');
      const coinNameInput = document.getElementById('coinNameInput');

      const subscriptionData = {
          email: emailInput.value,
          coin_name: coinNameInput.value
      };

      fetch('/subscriptions', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify(subscriptionData)
      })
          .then(response => response.json())
          .then(data => {
              console.log(data);
              emailInput.value = '';
              coinNameInput.value = '';
              loadSubscriptions();
          });
  });
});

function loadSubscriptions() {
  const subscriptionList = document.getElementById('subscriptionList');
  subscriptionList.innerHTML = '';

  fetch('/subscriptions')
      .then(response => response.json())
      .then(subscriptions => {
          subscriptions.forEach(subscription => {
              const li = document.createElement('li');
              li.textContent = `Email: ${subscription.email}, Coin Name: ${subscription.coin_name}`;
              subscriptionList.appendChild(li);
          });
      });
}
