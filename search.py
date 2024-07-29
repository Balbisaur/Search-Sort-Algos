def binary_search(arr, target):
    low, high = 0, len(arr) - 1  # Initialize low and high pointers
    
    while low <= high:  # Continue searching while the range is valid
        mid = (low + high) // 2  # Calculate the mid-point
        if arr[mid] == target:  # Check if mid-point is the target
            return mid  # Returning the index if found
        elif arr[mid] < target:  # If mid-point is less than target, move the low pointer up
            low = mid + 1
        else:  # If mid-point is greater than target, move the high pointer down
            high = mid - 1
            
    return -1  # Returning -1 if the target is not found

def sort_titles(titles):
    return sorted(titles)  # Returning the sorted list of titles

if __name__ == "__main__":
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

    sorted_titles = sort_titles(video_titles)  # Sorting the video titles
    search_title = "Digital Photography Essentials"  # searching for certain video
    index = binary_search(sorted_titles, search_title)  # Perform binary search

    if index != -1:  # Checking if the title was found
        print(f"Video found: {sorted_titles[index]}")  # Printing the found title
    else:
        print("Video not found.")  # Printing not found message

