# CAPSTONE

## Abstract

This is a platform where people can enjoy solving quizzes and post own quizzes.

## Distinctiveness and complexity

* **Compared to Project 1 Wiki**: Similar to Wiki in that it has the ability to accept user posts, this app is a quiz-answering platform, allowing users to submit answers and have them graded.

* **Compared to Project 2 Commerce**: The function that allows other users to react to what the user has posted is similar to the "auction" and "comment" functions of the e-commerce site created in Project 2. However, this application has a user profile page that allows users to view the past results of any user's answers.

* **Compared to Project 4 Network**: One of the more complex aspects of this app compared to Project 4 is its use of TailwindCSS. In previous projects, I used Bootstrap as the CSS framework, but for this application, adopted TailwindCSS for more flexible styling. 
  * This makes it easier to style elements as hover or not, and improves the UI. 
  * More colors can be used to customize the look and feel of the website.

## Features

The major functions of this app are as follows:

* **Display Quizzes**: Users including guests can see all quizzes from all users, with the most recent quiz first. This page should display:
  * ✅ title of the quiz
  * ✅ star: number of stars that the quiz have gained
  * ✅ author: the user who posted the quiz
  * ✅ timestamp: when the quiz is posted
  * ✅ status (login required): whether the quiz has already been solved, has not yet been solved, or whether they have submitted an answer but have not yet reached a correct answer.

* **View Quiz**: Users including guests can see detail of a quiz. This page should display:
  * ✅ title of the quiz
  * ✅ body of the quiz
  * who is the author
    * This is a link that takes you to the user's profile page when clicked.
  * ✅ timestamp when it was posted
  * ✅ form to submit answer
  * ✅ correct answer rate
    * The correct answer rate is a percentage of 100, which indicates what percentage of "users who submitted answers" arrived at the correct answer.

* ✅ **Post a New Quiz**: Users who are signed in should be able to write a new text-based quiz by filling in text into a text area and then clicking a button to submit the quiz.
  * To maintain consistency with the answers, quizzes cannot be edited once submitted.

* ✅ **Answer Quizzes**: Users who are signed in can answer problems. When they submit their answers, the submissions are automatically graded and the results are displayed.

* ✅ **Pagination**: Quizzes should only be displayed 5 on a page. If there are more than ten quizzes, a “Next” button should appear to take the user to the next page of quizzes. If not on the first page, a “Previous” button should appear to take the user to the previous page of quizzes as well.

* **Add or Remove Stars**: ✅ Users who are signed in are able to add and remove star to quizzes.

* **User Profile**: Users including guests can see each user's profile page. This page should display:
  * ✅ all of the quizzes the user has posted
  * ✅ the number of stars that user have gained
  * ✅ the number of quizzes that user have ever solved
  * ✅ all of the submissions for that user

* **Responsive Design**: ✅ The site's UI does not collapse regardless of user's screen size.

### On feature

### On implementation

## How to run this application
