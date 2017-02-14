game_id = "";

function turn(o) {
  idx = parseInt(o.id.substring(1, 2));
  y = Math.floor(idx / 3);
  x = idx % 3;
  $.post("/set/" + game_id + "/" + x + "/" + y, function(data) {
    if (data.error != "OK") {
      display_error(data.error);
    }
    get_status();
  }).fail(function() {
    set_status("Error.");
  })
}

function display_error(msg) {
  $("#error_msg").html(msg);
  $("#error_msg").fadeIn("fast");
  setTimeout(function () {
    $("#error_msg").fadeOut("slow");
  }, 1000);
}

function draw_board(board) {
  for (var i = 0; i < board.length; i++) {
    $("#f" + i).html(board[i]);
  }
}

function get_status() {
  $.get("/status/" + game_id, function(data) {
    draw_board(data.game.board);
    switch (data.game.status) {
      case "WAITING_FOR_HUMAN":
        set_status("It's your turn!");
        break;
      case "WAITING_FOR_AI":
        set_status("AI is thinking ...");
        setTimeout(get_status, 300);
        break;
      case "HUMAN_WINS":
        set_status("You won!");
        play_again();
        break;
      case "AI_WINS":
        set_status("AI won!");
        play_again();
        break;
      case "DRAW":
        set_status("Draw!");
        play_again();
        break;
      default:
        set_status("Unknown status.");
    }
  }).fail(function() {
    set_status("Error.");
  })
}

function play_again() {
  $("#play_again").fadeIn("fast", function() {});
}

function set_status(msg) {
  $("#status_msg").html(msg);
}

function new_game() {
  $("#play_again").hide();
  $.post("/new", function(data) {
    game_id = data.uid;
    get_status();
  }).fail(function() {
    set_status("Error.");
  });
}

new_game()
