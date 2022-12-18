# from flask import Flask, render_template, request, redirect
# from flask import Blueprint
# from models.player_history import Player_history
# import repositories.player_history_repository as player_history_repository
# import repositories.player_repository as player_repository
# import repositories.campaign_repository as campaign_repository

# players_history_blueprint = Blueprint("players_history", __name__)

# @visits_blueprint.route("/visits")
# def visits():
#     visits = visit_repository.select_all() # NEW
#     return render_template("visits/index.html", visits = visits)

# # NEW
# # GET '/visits/new'
# @visits_blueprint.route("/visits/new", methods=['GET'])
# def new_task():
#     users = user_repository.select_all()
#     locations = location_repository.select_all()
#     return render_template("visits/new.html", users = users, locations = locations)

# # CREATE
# # POST '/visits'
# @visits_blueprint.route("/visits",  methods=['POST'])
# def create_task():
#     user_id = request.form['user_id']
#     location_id = request.form['location_id']
#     review = request.form['review']
#     user = user_repository.select(user_id)
#     location = location_repository.select(location_id)
#     visit = Visit(user, location, review)
#     visit_repository.save(visit)
#     return redirect('/visits')


# # DELETE
# # DELETE '/visits/<id>'
# @visits_blueprint.route("/visits/<id>/delete", methods=['POST'])
# def delete_task(id):
#     visit_repository.delete(id)
#     return redirect('/visits')


