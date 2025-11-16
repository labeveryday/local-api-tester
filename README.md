# Local API Tester

![exmaple](./images/example.jpeg)

A professional, feature-rich API testing tool for local development. Built with Python and Flask, it provides a modern web interface with advanced features like environment variables, authentication presets, request history, and beautiful JSON syntax highlighting.

Perfect for testing local APIs, AWS API Gateway endpoints, Cognito-protected APIs, and any HTTP-based service.

## ✨ Features

### Core Functionality
- **HTTP Methods**: GET, POST, PUT, PATCH, DELETE
- **Custom Headers**: Add any headers in JSON format
- **Request Body**: Full support for JSON, form data, and text
- **Response Display**: Syntax-highlighted JSON with color-coded status badges

### Advanced Features
- **Environment Variables**: Define variables like `{{BASE_URL}}` and reuse across requests
- **Authentication Presets**: Quick setup for Bearer Token, Basic Auth, and API Key
- **Request History**: Automatically saves your last 50 requests
- **Saved Collections**: Organize and reuse frequently used requests
- **Response Metrics**: Track response time, size, and HTTP status
- **Modern UI**: Professional gradient design with two-panel layout

### Privacy & Speed
- **100% Local**: All data stored in your browser's localStorage
- **No External Dependencies**: No cloud services or external tracking
- **Fast**: Instant response with no network overhead

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/labeveryday/local-api-tester.git
   cd local-api-tester
   ```

2. **Set up virtual environment** (recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask requests
   ```

4. **Start the application**
   ```bash
   python app.py
   ```

5. **Open in browser**

   Navigate to `http://localhost:5000`

## 📖 How to Use

### Basic Request
1. Enter your API endpoint URL
2. Select HTTP method (GET, POST, PUT, PATCH, DELETE)
3. Add headers in JSON format (optional)
4. Add request body for POST/PUT/PATCH (optional)
5. Click **Send Request**

### Using Environment Variables
1. Click **Manage Environments** in the sidebar
2. Create a new environment (e.g., "Production")
3. Add variables: `BASE_URL`, `API_KEY`, etc.
4. In your request, use `{{BASE_URL}}/api/users`
5. Variables automatically replace before sending

### Authentication Presets
1. Select the **Auth** tab in the request builder
2. Choose authentication type:
   - **Bearer Token**: For OAuth 2.0 and JWT
   - **Basic Auth**: Username and password
   - **API Key**: Custom header with your API key
3. Enter credentials - headers are automatically configured

### Saving Requests
1. After sending a request, click **Save to Collection**
2. Give it a name (e.g., "Get User Profile")
3. Access saved requests from the sidebar
4. Click to instantly load and resend

### Request History
- Last 50 requests automatically saved
- Click any history item to reload it
- Clear history with the **Clear** button

## 🧪 Test APIs

Try these free public APIs to get started:

| API | Endpoint | Description |
|-----|----------|-------------|
| **JSONPlaceholder** | `https://jsonplaceholder.typicode.com/posts/1` | Fake REST API for testing |
| **Dog CEO** | `https://dog.ceo/api/breeds/image/random` | Random dog images |
| **Cat Facts** | `https://catfact.ninja/fact` | Random cat facts |
| **Pokemon** | `https://pokeapi.co/api/v2/pokemon/ditto` | Pokemon information |
| **Random User** | `https://randomuser.me/api/` | Generate random user data |
| **REST Countries** | `https://restcountries.com/v3.1/name/united` | Country information |
| **Jokes** | `https://official-joke-api.appspot.com/random_joke` | Random jokes |

### Example: Using Environment Variables
1. Create environment "JSONPlaceholder API"
2. Add variable: `BASE_URL` = `https://jsonplaceholder.typicode.com`
3. Test GET: `{{BASE_URL}}/posts/1`
4. Test POST: `{{BASE_URL}}/posts` with body: `{"title": "Test", "body": "Content", "userId": 1}`

## ☁️ AWS Deployment

For deploying to AWS Lambda with API Gateway, see the [aws_deployment](./aws_deployment/) directory which includes:
- AWS SAM template with CloudFront, WAF, and rate limiting
- Lambda-compatible Flask application
- Full deployment instructions

## 🎨 Customization

- **UI Styling**: Edit `templates/index.html` (uses Bootstrap 5)
- **Port Configuration**: Change `app.run(debug=True)` in `app.py` to specify host/port
- **Default Settings**: Modify JavaScript constants in the HTML template

## 🔒 Security Note

**This tool is designed for local development and testing.**

- ✅ Safe for local API testing
- ✅ Safe for testing development/staging endpoints
- ⚠️ Do not deploy publicly without authentication
- ⚠️ Do not use for production-critical operations
- ⚠️ Be cautious with sensitive API keys (they're stored in browser localStorage)

## 🤔 Why Use This?

**vs. Postman/Insomnia**
- ✅ Lightweight - no heavy desktop app
- ✅ Instant startup - just run Python
- ✅ Privacy-first - all data stays local
- ✅ Free forever - no account required
- ✅ Customizable - full access to source code

**vs. cURL**
- ✅ Visual interface - no command memorization
- ✅ Request history - easily replay requests
- ✅ Environment management - switch contexts quickly
- ✅ Response formatting - beautiful JSON display

## 🐛 Troubleshooting

**Application won't start**
```bash
# Ensure you're in the virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Reinstall dependencies
pip install --force-reinstall flask requests
```

**Environment variables not replacing**
- Ensure your variable names match exactly (case-sensitive)
- Variables should use format: `{{VARIABLE_NAME}}`
- Check that the correct environment is selected in the dropdown

**Response not displaying**
- Check browser console for JavaScript errors (F12)
- Verify the API endpoint is accessible
- Check CORS if testing cross-origin requests

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 About the Author

My passions lie in Network Engineering, Cloud Computing, Automation, and impacting people's lives. I'm fortunate to weave all these elements together in my role as a Developer Advocate. On GitHub, I share my ongoing learning journey and the projects I'm building. Don't hesitate to reach out for a friendly hello or to ask any questions!

**Connect with me:**
- [LinkedIn](https://www.linkedin.com/in/duanlightfoot/)
- [YouTube](https://www.youtube.com/@LabEveryday)

---

**⭐ If you find this tool useful, please consider giving it a star!**
