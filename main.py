import dblp_api
import crossref_api
import scrape_scientist

def main_by_author(author_name):
    """
    Main function

    :params: - author_name (str) the author name
    :returns: /
    """
    print('\n----'+len(author_name)*'-'+'----\n'+'*** '+author_name+' ***\n'+'----'+len(author_name)*'-'+'----')
    
    # DBLP
    print("\n--------\n| DBLP |\n--------\n")
    publications_from_dblp = dblp_api.get_articles_by_author(author_name)
    dblp_api.save_articles_into_database(publications_from_dblp,author_name,True)
    dblp_api.test_accuracy_author_name(author_name,publications_from_dblp,True)

    # Crossref
    print("\n------------\n| Crossref |\n------------\n")
    publications_from_crossref = crossref_api.get_articles_by_author(author_name)
    crossref_api.save_articles_into_database(publications_from_crossref,author_name,True)
    crossref_api.test_accuracy_author_name(author_name,publications_from_crossref,True)

    

def main():
    """
    Main function

    :params: /
    :returns: /
    """
    CRISTAL_permanent_members = scrape_scientist.recover_all_cristal_members()['permanent']

    for member_name in CRISTAL_permanent_members :
        print('________________________________________________________________')
        print('\n----'+len(member_name)*'-'+'----\n'+'*** '+member_name+' ***\n'+'----'+len(member_name)*'-'+'----')
    
        # DBLP
        print("\n--------\n| DBLP |\n--------\n")
        publications_from_dblp = dblp_api.get_articles_by_author(member_name)
        dblp_api.save_articles_into_database(publications_from_dblp,member_name,True)
        dblp_api.test_accuracy_author_name(member_name,publications_from_dblp,True)

        # Crossref
        print("\n------------\n| Crossref |\n------------\n")
        publications_from_crossref = crossref_api.get_articles_by_author(member_name)
        crossref_api.save_articles_into_database(publications_from_crossref,member_name,True)
        crossref_api.test_accuracy_author_name(member_name,publications_from_crossref,True)
    

if __name__ == "__main__": # execute only if run as a script
    
    #author_name=input("Write an author name : ")
    #main_by_author(author_name)

    main()
