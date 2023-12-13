from wiki import article_titles, ask_search, ask_advanced_search
# 1) 
#
# Function: search
#
# Parameters:
#   keyword - search word to look for in article titles
#
# Returns: list of article titles containing given keyword (case insensitive).
# If the keyword is empty or no results are found, return an empty list.
#
def search(keyword):
    if keyword == '':
        return []
    else:
        res = []
        keyword = keyword.lower()
        for i in article_titles():
            new = i.lower()
            if keyword in new:
                res.append(i)
        return res

# 2) 
#
# Function: title_length
#
# Returns 
#
# Parameters:
#   max_length - max character length of article titles
#   titles - list of article titles to search through
#
# Returns: list of article titles from given titles with a length that does
# not exceed max_length number of characters 
def title_length(max_length, titles):
    res = []
    for i in titles:
        if len(i) <= max_length:
            res.append(i)
    return res

# 3) 
#
# Function: article_count
#
# Parameters:
#   count - max number of returned articles
#   titles - list of article titles to search through
#
# Returns: list of articles in given titles starting from the 
# beginning that do not exceed given count in total. If there are no 
# given article titles, return an empty list regardless of the count.
# If the max is larger than the # of titles, returns all titles.
def article_count(count, titles):
    res = []
    if len(titles) == 0:
        return res
    elif count > len(titles):
        return titles
    else:
        for num in range(count):
            res.append(titles[num])
        return res

# 4) 
#
# Function: random_article
#
# Parameters:
#   index - index at which article title to return
#   titles - list of article titles to search through
#
# Returns: article title in given titles at given index. If
# index is not valid, returns an empty string
def random_article(index, titles):
    res = ''
    if index in range(len(titles)):
        res = titles[index]
    return res

# 5) 
#
# Function: favorite_article
#
# Parameters:
#   favorite - favorite article title
#   titles - list of article titles to search through
#
# Returns: True if favorite article is in the given articles
# (case insensitive) and False otherwise
def favorite_article(favorite, titles):
    new_fav = favorite.lower()
    for title in titles:
        new_title = title.lower()
        if new_fav == new_title:
            return True
    return False

# 6) 
#
# Function: multiple_keywords
#
# Parameters:
#   keyword - additional keyword to search
#   titles - list article titles resulting from basic search
#
# Returns: searches for article titles from entire list of available
# articles (from wiki) and adds those articles to list of article
# titles from basic search. Article titles should be returned as a list
# with all of the article titles from the new search coming after the
# original titles. Any duplicate titles may be listed twice.
def multiple_keywords(keyword, titles):
    if keyword == '':
        return titles
    else:
        res = []
        keyword = keyword.lower()
        for title in article_titles():
            new_title = title.lower()
            if keyword in new_title:
                res.append(title)
    res = titles + res
    return res

# Prints out articles based on searched keyword and advanced options
def display_result():
    # Stores list of articles returned from searching user's keyword
    articles = search(ask_search())

    # advanced stores user's chosen advanced option (1-5)
    # value stores user's response in being asked the advanced option
    advanced, value = ask_advanced_search()

    if advanced == 1:
        # value stores max article title length in number of characters
        # Update article titles to contain only ones of the maximum length
        articles = title_length(value, articles)
    if advanced == 2:
        # value stores max number of articles
        # Update article titles to contain only the max number of articles
        articles = article_count(value, articles)
    elif advanced == 3:
        # value stores random number
        # Update articles to only contain the article title at index of the random number
        articles = random_article(value, articles)
    elif advanced == 4:
        # value stores article title
        # Store whether article title is in the search results into a variable named has_favorite
        has_favorite = favorite_article(value, articles)
    elif advanced == 5:
        # value stores keyword to search
        # Updated article titles to contain article titles from the first search and the second search
        articles = multiple_keywords(value, articles)

    print()

    if not articles:
        print("No articles found")
    else:
        print("Here are your articles: " + str(articles))

    if advanced == 4:
        print("Your favorite article is" + ("" if has_favorite else " not") + " in the returned articles!")

if __name__ == "__main__":
    display_result()
