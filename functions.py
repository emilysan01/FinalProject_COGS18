import pandas as pd

# introduction to help build skincare regimen
introduction = input("""Lets help build your skincare regimen! 
Answer the following questions to figure out the best
cleanser, moisturizer, and sunscreen for you based on your budget.
Please note the prices are pre-tax. 

Enter your name to begin! """)

# define global namespace variables
reco = "I recommend: "
budget = "How many dollars would you spend on a "
total_products = "Your total for the products is $"
output = []

def cleanser():
    """Determines the best cleanser for the client based on budget. 
    
    Parameters
    ----------
    None.
    
    Returns
    -------
    reco : string
        Adds a comment for recommendation. 
    result : string
        Inputs the recommended cleanser.
    """
    
    # inquire budget for cleanser
    c_budget = int(input("\n" + budget + "cleanser? \n"))
    
    # create a dictionary for different types of cleansers
    c_dict = {"CeraVe Hydrating Cream to Foam Cleanser" : 14, 
              "First Aid Beauty Face Cleanser" : 34, 
              "La Prairie Purifying Cream Cleanser" : 95}
    
    # create conditions to determine best cleanser based on budget
    if c_budget < 14:
        return reco + "increasing your budget (:" + " \n"
    elif c_budget >= 14 and c_budget < 34:
        result = "CeraVe Hydrating Cream to Foam Cleanser"
        result_price = c_dict[result]
        output.append(result_price)
        return reco + result + " \n"
    elif c_budget >= 34 and c_budget < 95:
        result = "First Aid Beauty Face Cleanser"
        result_price = c_dict[result]
        output.append(result_price)
        return reco + result + " \n"
    elif c_budget >= 95 and c_budget <= 130:
        result = "La Prairie Purifying Cream Cleanser"
        result_price = c_dict[result]
        output.append(result_price)
        return reco + result + " \n"
    elif c_budget > 130:
        return reco + "NOT SPENDING THIS MUCH ON A SKINCARE PRODUCT?!4#$@#^$#^%" + " \n"
    
print(cleanser())

def moisturizer():
    """Determines the best moisturizer for the client based on budget. 
    
    Parameters
    ----------
    None.
    
    Returns
    -------
    reco : string
        Adds a comment for recommendation. 
    result : string
        Inputs the recommended moisturizer.
    """
    
    # inquire budget for moisturizer
    m_budget = int(input(budget + "moisturizer? \n"))

    # create a dictionary for different types of moisturizers
    m_dict = {"CeraVe Moisturizing Cream" : 10, 
              "First Aid Beauty Ultra Repair Cream" : 46, 
              "Skinceuticals Triple Lipid Restore 2:4:2" : 130}
    
    # create conditions
    if m_budget < 10:
        return reco + "increasing your budget (:" + " \n"
    elif m_budget >= 10 and m_budget < 46:
        result = "CeraVe Moisturizing Cream"
        result_price = m_dict[result]
        output.append(result_price)
        return reco + result + " \n"
    elif m_budget >= 46 and m_budget < 130:
        result = "First Aid Beauty Ultra Repair Cream"
        result_price = m_dict[result]
        output.append(result_price)
        return reco + result + " \n"
    elif m_budget == 130:
        result = "Skinceuticals Triple Lipid Restore 2:4:2"
        result_price = m_dict[result]
        output.append(result_price)
        return reco + result + " \n"
    elif m_budget > 130:
        return reco + "NOT SPENDING THIS MUCH ON A SKINCARE PRODUCT?!4#$@#^$#^%" + " \n"
    
print(moisturizer())

def sunscreen():
    """Determines the best sunscreen for the client based on budget. 
    
    Parameters
    ----------
    None.
    
    Returns
    -------
    reco : string
        Adds a comment for recommendation. 
    result : string
        Inputs the recommended sunscreen.
    """
    
    # inquire budget for sunscreen
    s_budget = int(input(budget + "sunscreen? \n"))
    
    # create a dictionary for different types of sunscreens
    s_dict = {"CeraVe AM Facial Moisturizing Lotion SPF 30" : 13, 
              "First Aid Beauty # 5 in 1 Face Cream SPF 30" : 40, 
              "La Mer Broad Spectrum SPF 50 UV Protecting Fluid" : 95}
    
    # create conditions
    if s_budget < 13:
        return reco + "increasing your budget (:" + " \n"
    elif s_budget >= 13 and s_budget < 40 :
        result = "CeraVe AM Facial Moisturizing Lotion SPF 30"
        result_price = s_dict[result]
        output.append(result_price)
        return reco + result + " \n"
    elif s_budget >= 40 and s_budget < 95:
        result = "First Aid Beauty # 5 in 1 Face Cream SPF 30"
        result_price = s_dict[result]
        output.append(result_price)
        return reco + result + " \n"
    elif s_budget >= 95 and s_budget <= 130:
        result = "La Mer Broad Spectrum SPF 50 UV Protecting Fluid"
        result_price = s_dict[result]
        output.append(result_price)
        return reco + result + " \n"
    elif s_budget > 130:
        return reco + "NOT SPENDING THIS MUCH ON A SKINCARE PRODUCT?!4#$@#^$#^%" + " \n"
    
print(sunscreen())

def calculate_total():
    """Calculates the total for each product recommended.
    
    Parameters
    ----------
    None.
    
    Returns
    -------
    total_products : string
        Comment before displaying total price of products.
    total : integer or string
        Shows total price of product recommendations.
    """
    
    total_cost = input("""We just helped pick your products! 
Now let's calculate the total cost of recommended skincare products.
Type anything in the chatbox to continue. \n""")
    
    # initialize total to 0
    total = 0 
    
    for val in output:
        total = total + val
        
    print()
    print(total_products + str(total) + " \n")

calculate_total()

def skincare():
    """Displays a chart that breaks down the price for each product.
    
    Note: To align the chart text to the left, I copied code from an external source:
    "https://www.geeksforgeeks.org/align-columns-to-left-in-pandas-python/"
    
    Parameters
    ----------
    None.
    
    Returns
    -------
    align : DataFrame
        Shows chart of products and aligns text to the left. 
    """
    
    chart = input("""If you're curious about the price of each product,
type anything in the chatbox to see the breakdown! \n""")
    
    # create a dictionary for the products and their prices
    data = {"Product" : ["CeraVe Hydrating Cream to Foam Cleanser", 
                        "First Aid Beauty Face Cleanser",
                        "La Prairie Purifying Cream Cleanser", 
                        "CeraVe Moisturizing Cream",
                        "First Aid Beauty Ultra Repair Cream",
                        "Skinceuticals Triple Lipid Restore 2:4:2",
                        "CeraVe AM Facial Moisturizing Lotion SPF 30",
                        "First Aid Beauty # 5 in 1 Face Cream SPF 30",
                        "La Mer Broad Spectrum SPF 50 UV Protecting Fluid"],
                        "Price" : ["$14", "$34", "$95", "$10" , "$46", "$130", "$13", "$40", "$95"]}

    df = pd.DataFrame(data)
    align = df.style.set_properties(**{'text-align': 'left'})
    
    align = align.set_table_styles(
    [dict(selector = 'th', props=[('text-align', 'left')])])

    display(align)

skincare()