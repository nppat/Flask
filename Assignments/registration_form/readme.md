Create a simple registration page with the following fields:
- email [x]
- first_name [x]
- last_name [x]
- password [x] 
- confirm_password [x]

Here are the validations you must include:
- All fields are required and must not be blank [x]
- First and Last Name cannot contain any numbers [x]
- Password should be more than 8 characters [x]
- Email should be a valid email [x]
- Password and Password Confirmation should match [x]

Ninja mode:
- Add the validation that requires a password to have at least 1 uppercase letter and 1 numeric value [ ]

Hacker mode:
- Add a birth-date field that must be validated as a valid date (and must be from the past) [ ]

When the form is submitted, make sure the user submits appropriate information. If the user did not submit appropriate information, return the error(s) above the form that asks the user to correct the information.