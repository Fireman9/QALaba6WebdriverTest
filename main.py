from selenium import webdriver
import time


def get_top_habr_news():
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.get("https://habr.com/ru/top/")
    posts = driver.find_elements_by_class_name("post__title_link")
    print("Top 3 post for today:")
    print_top_3_posts(posts)

    driver.find_element_by_class_name("tabs").find_element_by_link_text("Неделя").click()
    posts = driver.find_elements_by_class_name("post__title_link")
    print("Top 3 post for week:")
    print_top_3_posts(posts)

    driver.find_element_by_class_name("tabs").find_element_by_link_text("Месяц").click()
    posts = driver.find_elements_by_class_name("post__title_link")
    print("Top 3 post for month:")
    print_top_3_posts(posts)

    driver.find_element_by_class_name("tabs").find_element_by_link_text("Год").click()
    posts = driver.find_elements_by_class_name("post__title_link")
    print("Top 3 post for year:")
    print_top_3_posts(posts)

    driver.close()


def print_top_3_posts(posts):
    for i in range(3):
        print(posts[i].text, end=": ")
        print(posts[i].get_property("href"))


if __name__ == '__main__':
    get_top_habr_news()
