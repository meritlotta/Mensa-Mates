# helper for ranking
def load_user_rankings(username):
    rankings = []

    with open("ranking.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        current = {}
        collecting_feedback = False
        feedback = []

        for line in lines:
            line = line.strip()

            if line.startswith("Username:"):
                current_user = line.split(":", 1)[1].strip()
                collecting_feedback = False
                current = {}

            elif line.startswith("Item:"):
                current["item"] = line.split(":", 1)[1].strip()

            elif line.startswith("Ranking:"):
                current["ranking"] = line.split(":", 1)[1].strip()

            elif line == "Feedback:":
                collecting_feedback = True
                feedback = []

            elif line == "-" * 40:
                if current_user == username:
                    current["feedback"] = feedback[:]
                    rankings.append(current.copy())
                current = {}
                feedback = []
                collecting_feedback = False

            elif collecting_feedback:
                feedback.append(line)
    return rankings
