from flask import Flask, request, jsonify
from search import binary_search, sort_titles

app = Flask(__name__)

video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

sorted_titles = sort_titles(video_titles)

@app.route('/search', methods=['GET'])# GET request methods for search results 
def search_video():
    title = request.args.get('title')# get title from request
    if not title:
        return jsonify({"error": "Title query parameter is required"}), 400 # 404 error message 
    
    index = binary_search(sorted_titles, title)
    
    if index != -1: 
        return jsonify({"message": "Video found", "title": sorted_titles[index]}), 200 
    else:
        return jsonify({"message": "Video not found"}), 404 # error message is video not found

if __name__ == '__main__':
    app.run(debug=True)
