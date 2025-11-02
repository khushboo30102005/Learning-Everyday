const myForm = document.getElementById('myForm');
const emailInput = document.getElementById('emailInput');
const passwordInput = document.getElementById('passwordInput');
const message = document.getElementById('message');
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Basic email format
const passwordRegex =
  /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/; // Strong password

myForm.addEventListener('submit', (e) => {
  e.preventDefault();
  message.classList.remove('text-green-800', 'text-red-800');
    const email = emailInput.value.trim();
  const password = passwordInput.value.trim();
  if (email === '' || password === '') {
    message.innerText = '⚠️ Please fill all inputs';
    message.classList.add('text-red-800');
    return;
  }
  if (!emailRegex.test(email)) {
    message.innerText = '❌ Invalid Email Format';
    message.classList.add('text-red-800');
    return;
  }
  if (!passwordRegex.test(password)) {
    message.innerText = '❌ Password must be at least 8 characters.';
    message.classList.add('text-red-800', 'text-sm');
    return;
  }
  message.innerText = '✅ Login Successful! 🎉';
  message.classList.add('text-green-800');
});
