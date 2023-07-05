---
description: >-
  # This project is a very basic Tic Tac Toe game created with Pygame for
  Python.
---

# Tic Tac Toe

### Features&#x20;

* The board size k can be set to any number within the main.py file

<pre class="language-python" data-title="main.py" data-line-numbers data-full-width="false"><code class="lang-python">if __name__ == "__main__":
        <a data-footnote-ref href="#user-content-fn-1">board_size = </a>3
        ttt = TicTacToe(board_size)
        ttt.run()
<strong>
</strong></code></pre>

* The game currently only allows for player versus player.
* Once a game has finished and the user has clicked the screen, a new game instance is started.
* All valid position are highlighted green
* All invalid positions are highlighted yellow.
* Any time a user clicks a square a yellow highlight is show on the square to show they have selected it.
* The board will go completely red if there is no winner (I.e. there is a draw)
* Upon any instance where there are k same symbols in a row, this row will highlight yellow.

### Demonstration

<div align="center">

<img src="https://media.giphy.com/media/9kV2r0AzcC23PMtozt/giphy.gif" alt="4X4">

</div>





<div align="center">

<img src="https://media.giphy.com/media/9hgXVmpEj7nHwFOrkn/giphy.gif" alt="3X3">

</div>

### Limitations

I think there is a lot too improve upon in this project but I am unable to fully see where these areas are as I have only just begun learning the Pygame framework.&#x20;

Naturally, the concept of a 100X100 board of Tic Tac Toe is absurd - It would certainly be a long game. Nevertheless, to truly better my programming skills I am trying to focus upon scalability. If I am to return to this project everything should be inline with good OOP principles such as: well encapsulated objects and low coupling, such that if I do return, I'm not served up a disaterous bowl of Spaghetti Bolognese.&#x20;

My aim with all these small project is such that it would be possible to return and easily add upon the project without everything collapsing upon me

#### `Why?`

This project is really intended to practice my OO skills as well as gain a stronger grasp on the PyGame framework.&#x20;

For this years large project aim, I have set myself the challenge of creating an automated chess board, not only in python and pygame but as a physical board in reality that one can manipulate. It certainly seem plausible and I making my way through towards this goal by starting with smaller projects.&#x20;

I know they're currently very simple but my main focus is to truly hone software development, object oriented programming and mathematical skills.

#### Written - 05/07/2023



[^1]: set to k
