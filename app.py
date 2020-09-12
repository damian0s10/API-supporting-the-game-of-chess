from flask import Flask, jsonify, abort
from chessboard import Chessboard
import chesspieces
from typing import List, Any, Tuple

app = Flask(__name__)


@app.route("/api/v1/<chess_figure>/<current_field>/", methods=["GET"])
@app.route("/api/v1/<chess_figure>/<current_field>/<dest_field>", methods=["GET"])
def available_fields(
    chess_figure: str, current_field: str, dest_field: str = None
) -> Tuple[Any, int]:

    try:
        error: str = None
        moves: List[str] = []
        error_code: int = 200

        chessboard: Chessboard = Chessboard()
        current_field: str = current_field.upper()

        if chessboard.validate_field(current_field):
            try:
                class_name = getattr(chesspieces, chess_figure.capitalize())
                obj = class_name(current_field)
                moves = obj.list_available_moves()

            except AttributeError:
                error = "Figure does not exist."
                error_code = 404

                return (
                    jsonify(
                        {
                            "availableMoves": moves,
                            "error": error,
                            "figure": chess_figure.lower(),
                            "currentField": current_field,
                        }
                    ),
                    error_code,
                )

            if dest_field:
                dest_field = dest_field.upper()
                move: str

                if chessboard.validate_field(dest_field):
                    if obj.validate_move(dest_field):
                        move = "valid"

                    else:
                        move = "invalid"
                        error = "Current move is not permitted."

                else:
                    move = "invalid"
                    error = "Destination field does not exist."
                    error_code = 409

                return (
                    jsonify(
                        {
                            "move": move,
                            "figure": chess_figure.lower(),
                            "error": error,
                            "currentField": current_field,
                            "destField": dest_field,
                        }
                    ),
                    error_code,
                )

        else:
            error = "Field does not exist."
            error_code = 409

        return (
            jsonify(
                {
                    "availableMoves": moves,
                    "error": error,
                    "figure": chess_figure.lower(),
                    "currentField": current_field,
                }
            ),
            error_code,
        )
    except:
        abort(500)


if __name__ == "__main__":

    app.run(debug=True, host="0.0.0.0")
