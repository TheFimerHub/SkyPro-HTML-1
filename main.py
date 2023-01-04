from flask import Flask, render_template
from utilits import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)

@app.route('/')
def main_page():
    candidates: list[dict] = load_candidates_from_json()
    return render_template('list.html', candidates=candidates)

@app.route('/candidate/<int:idx>')
def personal_page(idx):
    candidate: dict = get_candidate(idx)
    if not candidate:
        return "Кандидат не найден"
    return render_template('card.html', candidate=candidate)

@app.route('/search/<candidate_name>')
def search_name_page(candidate_name):
    candidates: list[dict] = get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates)

@app.route('/skill/<skill_name>')
def search_skills_page(skill_name):
    candidates: list[dict] = get_candidates_by_skill(skill_name)
    return render_template('skill.html', skill=skill_name, candidates=candidates)

app.run()