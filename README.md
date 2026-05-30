<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Page</title>
    <style>
        /* Global resets and centered alignment */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background: #f0f2f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        /* Card container for the form */
        .login-container {
            background: #ffffff;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
        }

        .login-container h2 {
            margin-bottom: 24px;
            color: #333333;
            text-align: center;
        }

        /* Form control styling */
        .form-group {
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            color: #666666;
            font-size: 14px;
        }

        .form-group input {
            width: 100%;
            padding: 12px;
            border: 1px solid #cccccc;
            border-radius: 4px;
            font-size: 16px;
            outline: none;
            transition: border-color 0.2s;
        }

        .form-group input:focus {
            border-color: #0066cc;
        }

        /* Utilities: Remember me & forgot password */
        .form-options {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 24px;
            font-size: 14px;
        }

        .form-options label {
            display: flex;
            align-items: center;
            gap: 6px;
            color: #666666;
            cursor: pointer;
        }

        .form-options a {
            color: #0066cc;
            text-decoration: none;
        }

        .form-options a:hover {
            text-decoration: underline;
        }

        /* Primary action button */
        .btn-submit {
            width: 100%;
            padding: 12px;
            background: #0066cc;
            color: #ffffff;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.2s;
        }

        .btn-submit:hover {
            background: #0052a3;
        }

        /* Secondary action link */
        .signup-link {
            text-align: center;
            margin-top: 20px;
            font-size: 14px;
            color: #666666;
        }

        .signup-link a {
            color: #0066cc;
            text-decoration: none;
            font-weight: 600;
        }

        .signup-link a:hover {
            text-decoration: underline;
OAOAOA        }
OAOAOA    </style>
OAOAOA</head>
<body>

    <div class="login-container">
OBOBOB        <h2>Account Login</h2>
        
OBOBOB        <!-- The data transfer is securely designated to use POST -->
        <form action="/login-endpoint" method="POST">
OBOBOB            
            <!-- Email Input Field -->
OBOBOB            <div class="form-group">
                <label for="email">Email Address</label>
                <input type="email" id="email" name="email" placeholder="example@domain.com" required>
            </div>
            
            <!-- Password Input Field -->
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" placeholder="Enter your password" required>
            </div>
            
            <!-- Auxiliary options -->
            <div class="form-options">
                <label>
                    <input type="checkbox" name="remember"> Remember me
                </label>
                <a href="#">Forgot Password?</a>
            </div>
            
            <!-- Submission element -->
            <button type="submit" class="btn-submit">Sign In</button>
            
        </form>
        
        <div class="signup-link">
            Don't have an account? <a href="#">Create one</a>
        </div>
    </div>

</body>
</html>
 
