import streamlit as st
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import random

def button_click():
    options = ["fact", "fact1", "fact2", "fact3", "fact4"]
    randomFact = random.choice(options)
    label["text"] = randomFact

def state_changed(event):
    selected_city.set("")  # Clear the selected city when state changes
    city_names=['']
    if selected_state.get() == "Alabama":
        city_names = ['Birmingham', 'Montgomery', 'Mobile', 'Huntsville', 'Tuscaloosa', 'Hoover', 'Dothan', 'Auburn', 'Decatur', 'Madison']
    elif selected_state.get() == "Alaska":
        city_names = ['Anchorage', 'Fairbanks', 'Juneau', 'Sitka', 'Ketchikan', 'Wasilla', 'Kenai', 'Kodiak', 'Bethel', 'Palmer']
    elif selected_state.get() == "Arizona":
        city_names = ['Phoenix', 'Tucson', 'Mesa', 'Chandler', 'Scottsdale', 'Glendale', 'Gilbert', 'Tempe', 'Peoria', 'Surprise']
    elif selected_state.get() == "Arkansas":
        city_names = ['Little Rock', 'Fort Smith', 'Fayetteville', 'Springdale', 'Jonesboro', 'North Little Rock', 'Conway', 'Rogers', 'Bentonville', 'Pine Bluff']
    elif selected_state.get() == "California":
        city_names = ['Los Angeles', 'San Diego', 'San Jose', 'San Francisco', 'Fresno', 'Sacramento', 'Long Beach', 'Oakland', 'Bakersfield', 'Anaheim']
    elif selected_state.get() == "Colorado":
        city_names = ['Denver', 'Colorado Springs', 'Aurora', 'Fort Collins', 'Lakewood', 'Thornton', 'Arvada', 'Westminster', 'Pueblo', 'Centennial']
    elif selected_state.get() == "Connecticut":
        city_names = ['Bridgeport', 'New Haven', 'Stamford', 'Hartford', 'Waterbury', 'Norwalk', 'Danbury', 'New Britain', 'West Hartford', 'Meriden']
    elif selected_state.get() == "Delaware":
        city_names = ['Wilmington', 'Dover', 'Newark', 'Middletown', 'Smyrna', 'Milford', 'Seaford', 'Georgetown', 'Elsmere', 'New Castle']
    elif selected_state.get() == "Florida":
        city_names = ['Jacksonville', 'Miami', 'Tampa', 'Orlando', 'St. Petersburg', 'Hialeah', 'Tallahassee', 'Fort Lauderdale', 'Port St. Lucie', 'Cape Coral']
    elif selected_state.get() == "Georgia":
        city_names = ['Atlanta', 'Augusta', 'Columbus', 'Savannah', 'Athens', 'Sandy Springs', 'Macon', 'Roswell', 'Albany', 'Johns Creek']
    elif selected_state.get() == "Hawaii":
        city_names = ['Honolulu', 'East Honolulu', 'Pearl City', 'Hilo', 'Kailua', 'Waipahu', 'Kaneohe', 'Mililani Town', 'Kahului', 'Ewa Gentry']
    elif selected_state.get() == "Idaho":
        city_names = ['Boise', 'Meridian', 'Nampa', 'Idaho Falls', 'Pocatello', 'Caldwell', 'Coeur d\'Alene', 'Twin Falls', 'Lewiston', 'Post Falls']
    elif selected_state.get() == "Illinois":
        city_names = ['Chicago', 'Aurora', 'Rockford', 'Joliet', 'Naperville', 'Springfield', 'Peoria', 'Elgin', 'Waukegan', 'Cicero']
    elif selected_state.get() == "Indiana":
        city_names = ['Indianapolis', 'Fort Wayne', 'Evansville', 'South Bend', 'Carmel', 'Fishers', 'Bloomington', 'Hammond', 'Gary', 'Lafayette']
    elif selected_state.get() == "Iowa":
        city_names = ['Des Moines', 'Cedar Rapids', 'Davenport', 'Sioux City', 'Iowa City', 'Waterloo', 'Ames', 'West Des Moines', 'Council Bluffs', 'Ankeny']
    elif selected_state.get() == "Kansas":
        city_names = ['Wichita', 'Overland Park', 'Kansas City', 'Olathe', 'Topeka', 'Lawrence', 'Shawnee', 'Manhattan', 'Lenexa', 'Salina']
    elif selected_state.get() == "Kentucky":
        city_names = ['Louisville', 'Lexington', 'Bowling Green', 'Owensboro', 'Covington', 'Hopkinsville', 'Richmond', 'Florence', 'Georgetown', 'Elizabethtown']
    elif selected_state.get() == "Louisiana":
        city_names = ['New Orleans', 'Baton Rouge', 'Shreveport', 'Lafayette', 'Lake Charles', 'Kenner', 'Bossier City', 'Monroe', 'Alexandria', 'Houma']
    elif selected_state.get() == "Maine":
        city_names = ['Portland', 'Lewiston', 'Bangor', 'South Portland', 'Auburn', 'Biddeford', 'Sanford', 'Augusta', 'Saco', 'Westbrook']
    elif selected_state.get() == "Maryland":
        city_names = ['Baltimore', 'Frederick', 'Rockville', 'Gaithersburg', 'Bowie', 'Hagerstown', 'Annapolis', 'College Park', 'Salisbury', 'Laurel']
    elif selected_state.get() == "Massachusetts":
        city_names = ['Boston', 'Worcester', 'Springfield', 'Lowell', 'Cambridge', 'New Bedford', 'Brockton', 'Quincy', 'Lynn', 'Fall River']
    elif selected_state.get() == "Michigan":
        city_names = ['Detroit', 'Grand Rapids', 'Warren', 'Sterling Heights', 'Ann Arbor', 'Lansing', 'Flint', 'Dearborn', 'Livonia', 'Westland']
    elif selected_state.get() == "Minnesota":
        city_names = ['Minneapolis', 'St. Paul', 'Rochester', 'Duluth', 'Bloomington', 'Brooklyn Park', 'Plymouth', 'St. Cloud', 'Eagan', 'Woodbury']
    elif selected_state.get() == "Mississippi":
        city_names = ['Jackson', 'Gulfport', 'Southaven', 'Hattiesburg', 'Biloxi', 'Meridian', 'Tupelo', 'Greenville', 'Olive Branch', 'Horn Lake']
    elif selected_state.get() == "Missouri":
        city_names = ['Kansas City', 'St. Louis', 'Springfield', 'Independence', 'Columbia', 'Lee\'s Summit', 'O\'Fallon', 'St. Joseph', 'St. Charles', 'Blue Springs']
    elif selected_state.get() == "Montana":
        city_names = ['Billings', 'Missoula', 'Great Falls', 'Bozeman', 'Butte-Silver Bow', 'Helena', 'Kalispell', 'Havre', 'Anaconda-Deer Lodge County', 'Miles City']
    elif selected_state.get() == "Nebraska":
        city_names = ['Omaha', 'Lincoln', 'Bellevue', 'Grand Island', 'Kearney', 'Fremont', 'Hastings', 'North Platte', 'Norfolk', 'Columbus']
    elif selected_state.get() == "Nevada":
        city_names = ['Las Vegas', 'Henderson', 'Reno', 'North Las Vegas', 'Sparks', 'Carson City', 'Fernley', 'Elko', 'Mesquite', 'Boulder City']
    elif selected_state.get() == "New Hampshire":
        city_names = ['Manchester', 'Nashua', 'Concord', 'Derry', 'Dover', 'Rochester', 'Salem', 'Merrimack', 'Hudson', 'Londonderry']
    elif selected_state.get() == "New Jersey":
        city_names = ['Newark', 'Jersey City', 'Paterson', 'Elizabeth', 'Trenton', 'Clifton', 'Camden', 'Passaic', 'Union City', 'Bayonne']
    elif selected_state.get() == "New Mexico":
        city_names = ['Albuquerque', 'Las Cruces', 'Rio Rancho', 'Santa Fe', 'Roswell', 'Farmington', 'Clovis', 'Hobbs', 'Alamogordo', 'Carlsbad']
    elif selected_state.get() == "New York":
        city_names = ['New York City', 'Buffalo', 'Rochester', 'Yonkers', 'Syracuse', 'Albany', 'New Rochelle', 'Mount Vernon', 'Schenectady', 'Utica']
    elif selected_state.get() == "North Carolina":
        city_names = ['Charlotte', 'Raleigh', 'Greensboro', 'Durham', 'Winston-Salem', 'Fayetteville', 'Cary', 'Wilmington', 'High Point', 'Concord']
    elif selected_state.get() == "North Dakota":
        city_names = ['Fargo', 'Bismarck', 'Grand Forks', 'Minot', 'West Fargo', 'Mandan', 'Dickinson', 'Jamestown', 'Williston', 'Wahpeton']
    elif selected_state.get() == "Ohio":
        city_names = ['Columbus', 'Cleveland', 'Cincinnati', 'Toledo', 'Akron', 'Dayton', 'Parma', 'Canton', 'Youngstown', 'Lorain']
    elif selected_state.get() == "Oklahoma":
        city_names = ['Oklahoma City', 'Tulsa', 'Norman', 'Broken Arrow', 'Lawton', 'Edmond', 'Moore', 'Midwest City', 'Enid', 'Stillwater']
    elif selected_state.get() == "Oregon":
        city_names = ['Portland', 'Salem', 'Eugene', 'Gresham', 'Hillsboro', 'Beaverton', 'Bend', 'Medford', 'Springfield', 'Corvallis']
    elif selected_state.get() == "Pennsylvania":
        city_names = ['Philadelphia', 'Pittsburgh', 'Allentown', 'Erie', 'Reading', 'Scranton', 'Bethlehem', 'Lancaster', 'Harrisburg', 'Altoona']
    elif selected_state.get() == "Rhode Island":
        city_names = ['Providence', 'Warwick', 'Cranston', 'Pawtucket', 'East Providence', 'Woonsocket', 'Coventry', 'Cumberland', 'North Providence', 'South Kingstown']
    elif selected_state.get() == "South Carolina":
        city_names = ['Columbia', 'Charleston', 'North Charleston', 'Mount Pleasant', 'Rock Hill', 'Greenville', 'Summerville', 'Sumter', 'Hilton Head Island', 'Spartanburg']
    elif selected_state.get() == "South Dakota":
        city_names = ['Sioux Falls', 'Rapid City', 'Aberdeen', 'Brookings', 'Watertown', 'Mitchell', 'Yankton', 'Pierre', 'Huron', 'Vermillion']
    elif selected_state.get() == "Tennessee":
        city_names = ['Nashville', 'Memphis', 'Knoxville', 'Chattanooga', 'Clarksville', 'Murfreesboro', 'Franklin', 'Jackson', 'Johnson City', 'Bartlett']
    elif selected_state.get() == "Texas":
        city_names = ['Houston', 'San Antonio', 'Dallas', 'Austin', 'Fort Worth', 'El Paso', 'Arlington', 'Corpus Christi', 'Plano', 'Laredo']
    elif selected_state.get() == "Utah":
        city_names = ['Salt Lake City', 'West Valley City', 'Provo', 'West Jordan', 'Orem', 'Sandy', 'Ogden', 'St. George', 'Layton', 'Taylorsville']
    elif selected_state.get() == "Vermont":
        city_names = ['Burlington', 'Essex', 'South Burlington', 'Colchester', 'Rutland', 'Bennington', 'Brattleboro', 'Hartford', 'Milton', 'Barre']
    elif selected_state.get() == "Virginia":
        city_names = ['Virginia Beach', 'Norfolk', 'Chesapeake', 'Richmond', 'Newport News', 'Alexandria', 'Hampton', 'Roanoke', 'Portsmouth', 'Suffolk']
    elif selected_state.get() == "Washington":
        city_names = ['Seattle', 'Spokane', 'Tacoma', 'Vancouver', 'Bellevue', 'Kent', 'Everett', 'Renton', 'Yakima', 'Spokane Valley']
    elif selected_state.get() == "West Virginia":
        city_names = ['Charleston', 'Huntington', 'Morgantown', 'Parkersburg', 'Wheeling', 'Weirton', 'Fairmont', 'Martinsburg', 'Beckley', 'Clarksburg']
    elif selected_state.get() == "Wisconsin":
        city_names = ['Milwaukee', 'Madison', 'Green Bay', 'Kenosha', 'Racine', 'Appleton', 'Waukesha', 'Oshkosh', 'Eau Claire', 'Janesville']
    elif selected_state.get() == "Wyoming":
        city_names = ['Cheyenne', 'Casper', 'Laramie', 'Gillette', 'Rock Springs', 'Sheridan', 'Green River', 'Evanston', 'Riverton', 'Cody']
    else:
        city_names = ['']

    # Update the city dropdown menu with the appropriate city names
    city_dropdown = ttk.Combobox(search_frame, textvariable=selected_city)

    # Create the state dropdown menu
    state_label = ttk.Label(window, text="State:")
    state_label.pack()
    state_dropdown = ttk.Combobox(window, textvariable=selected_state, state="readonly")
    state_dropdown.pack()
    state_dropdown.bind("<<ComboboxSelected>>", state_changed)

    # Create the city dropdown menu
    city_label = ttk.Label(window, text="City:")
    city_label.pack()
    city_dropdown = ttk.Combobox(window, textvariable=selected_city, state="readonly")
    city_dropdown.pack()

def city_changed(event):
    showinfo(
        title='Result',
        message=f'You selected {selected_city.get()}, {selected_state.get()}'
    )




### fun facts ###
window = tk.Tk()
window.geometry("1000x1000")
frame = tk.Frame(window, width = 1000, height = 30, bg = "black", highlightbackground="white", highlightthickness=2)
window.configure(background="black")
frame.pack(side="bottom", pady=40)

label = tk.Label(frame, width=50, height=5, text="fun fact", font=("Comic Sans Serif",12), fg="white", wraplength=200, bg="black", anchor=tk.NW)
label.pack()

button = tk.Button(frame, text="click for another", font=("Comic Sans MS", 11), bd=0, command=button_click, fg="white", activebackground="black", activeforeground="white")
button.configure(highlightbackground="black", highlightcolor="black")
button.pack(anchor = tk.S, side="right", padx=6, pady=1)




### search box for states frame ###
search_frame = tk.Frame(window, width=800, height=600, bg = "black", highlightbackground="white", highlightthickness=2)
search_frame.pack(padx=150, pady=100, anchor=tk.N, side="left")

label1 = tk.Label(search_frame, text="Please select a state:", font=("Comic Sans Serif",12), fg="white", wraplength=200, bg="black", anchor=tk.W)
label1.pack(fill=tk.X)

# create a combobox
selected_state = tk.StringVar()

state_names = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

# drop down box
state = ttk.Combobox(search_frame, textvariable=selected_state)
state['values'] = state_names
state.current(0)
state.bind('<<ComboboxSelected>>', state_changed)

# place the widget
state.pack(fill=tk.X, padx=5, pady=5)






### Information ###
city_info = {
    'Alabama': {
        'Birmingham': 'Information about Birmingham',
        'Montgomery': 'Information about Montgomery',
        'Mobile': 'Information about Mobile',
        'Huntsville': 'Information about Huntsville',
        'Tuscaloosa': 'Information about Tuscaloosa',
        'Hoover': 'Information about Hoover',
        'Dothan': 'Information about Dothan',
        'Auburn': 'Information about Auburn',
        'Decatur': 'Information about Decatur',
        'Madison': 'Information about Madison',
    },
    'Alaska': {
        'Anchorage': 'Information about Anchorage',
        'Fairbanks': 'Information about Fairbanks',
        'Juneau': 'Information about Juneau',
        'Sitka': 'Information about Sitka',
        'Ketchikan': 'Information about Ketchikan',
        'Wasilla': 'Information about Wasilla',
        'Kenai': 'Information about Kenai',
        'Kodiak': 'Information about Kodiak',
        'Bethel': 'Information about Bethel',
        'Palmer': 'Information about Palmer',
    },
    'Arizona': {
        'Phoenix': 'Information about Phoenix',
        'Tucson': 'Information about Tucson',
    },
    'Arkansas': {
        'Little Rock': 'Information about Little Rock',
        'Fort Smith': 'Information about Fort Smith',
        'Fayetteville': 'Information about Fayetteville',
    },
    # Add more states and their cities' information
    'California': {
        'Los Angeles': 'Information about Los Angeles',
        'San Francisco': 'Information about San Francisco',
        'San Diego': 'Information about San Diego',
    },
    'Colorado': {
        'Denver': 'Information about Denver',
        'Colorado Springs': 'Information about Colorado Springs',
        'Aurora': 'Information about Aurora',
    },
    'Connecticut': {
        'Bridgeport': 'Information about Bridgeport',
        'New Haven': 'Information about New Haven',
        'Hartford': 'Information about Hartford',
    },
    'Delaware': {
        'Wilmington': 'Information about Wilmington',
        'Dover': 'Information about Dover',
        'Newark': 'Information about Newark',
    },
    'Florida': {
        'Jacksonville': 'Information about Jacksonville',
        'Miami': 'Information about Miami',
        'Tampa': 'Information about Tampa',
    },
    'Georgia': {
        'Atlanta': 'Information about Atlanta',
        'Savannah': 'Information about Savannah',
        'Augusta': 'Information about Augusta',
    },
    'Hawaii': {
        'Honolulu': 'Information about Honolulu',
        'Hilo': 'Information about Hilo',
        'Kailua': 'Information about Kailua',
    },
    'Idaho': {
        'Boise': 'Information about Boise',
        'Meridian': 'Information about Meridian',
        'Nampa': 'Information about Nampa',
    },
    'Illinois': {
        'Chicago': 'Information about Chicago',
        'Springfield': 'Information about Springfield',
        'Peoria': 'Information about Peoria',
    },
    'Indiana': {
        'Indianapolis': 'Information about Indianapolis',
        'Fort Wayne': 'Information about Fort Wayne',
        'Evansville': 'Information about Evansville',
    },
    'Iowa': {
        'Des Moines': 'Information about Des Moines',
        'Cedar Rapids': 'Information about Cedar Rapids',
        'Davenport': 'Information about Davenport',
    },
    'Kansas': {
        'Wichita': 'Information about Wichita',
        'Overland Park': 'Information about Overland Park',
        'Kansas City': 'Information about Kansas City',
    },
    'Kentucky': {
        'Louisville': 'Information about Louisville',
        'Lexington': 'Information about Lexington',
        'Bowling Green': 'Information about Bowling Green',
    },
    'Louisiana': {
        'New Orleans': 'Information about New Orleans',
        'Baton Rouge': 'Information about Baton Rouge',
        'Shreveport': 'Information about Shreveport',
    },
    'Maine': {
        'Portland': 'Information about Portland',
        'Lewiston': 'Information about Lewiston',
        'Bangor': 'Information about Bangor',
    },
    'Maryland': {
        'Baltimore': 'Information about Baltimore',
        'Rockville': 'Information about Rockville',
        'Gaithersburg': 'Information about Gaithersburg',
    },
    'Massachusetts': {
        'Boston': 'Information about Boston',
        'Worcester': 'Information about Worcester',
        'Springfield': 'Information about Springfield',
    },
    'Michigan': {
        'Detroit': 'Information about Detroit',
        'Grand Rapids': 'Information about Grand Rapids',
        'Lansing': 'Information about Lansing',
    },
    'Minnesota': {
        'Minneapolis': 'Information about Minneapolis',
        'Saint Paul': 'Information about Saint Paul',
        'Rochester': 'Information about Rochester',
    },
    'Mississippi': {
        'Jackson': 'Information about Jackson',
        'Gulfport': 'Information about Gulfport',
        'Hattiesburg': 'Information about Hattiesburg',
    },
    'Missouri': {
        'Kansas City': 'Information about Kansas City',
        'Saint Louis': 'Information about Saint Louis',
        'Springfield': 'Information about Springfield',
    },
    'Montana': {
        'Billings': 'Information about Billings',
        'Missoula': 'Information about Missoula',
        'Great Falls': 'Information about Great Falls',
    },
    'Nebraska': {
        'Omaha': 'Information about Omaha',
        'Lincoln': 'Information about Lincoln',
        'Bellevue': 'Information about Bellevue',
    },
    'Nevada': {
        'Las Vegas': 'Information about Las Vegas',
        'Henderson': 'Information about Henderson',
        'Reno': 'Information about Reno',
    },
    'New Hampshire': {
        'Manchester': 'Information about Manchester',
        'Nashua': 'Information about Nashua',
        'Concord': 'Information about Concord',
    },
    'New Jersey': {
        'Newark': 'Information about Newark',
        'Jersey City': 'Information about Jersey City',
        'Paterson': 'Information about Paterson',
    },
    'New Mexico': {
        'Albuquerque': 'Information about Albuquerque',
        'Las Cruces': 'Information about Las Cruces',
        'Santa Fe': 'Information about Santa Fe',
    },
    'New York': {
        'New York City': 'Information about New York City',
        'Buffalo': 'Information about Buffalo',
        'Rochester': 'Information about Rochester',
    },
    'North Carolina': {
        'Charlotte': 'Information about Charlotte',
        'Raleigh': 'Information about Raleigh',
        'Greensboro': 'Information about Greensboro',
    },
    'North Dakota': {
        'Fargo': 'Information about Fargo',
        'Bismarck': 'Information about Bismarck',
        'Grand Forks': 'Information about Grand Forks',
    },
    'Ohio': {
        'Columbus': 'Information about Columbus',
        'Cleveland': 'Information about Cleveland',
        'Cincinnati': 'Information about Cincinnati',
    },
    'Oklahoma': {
        'Oklahoma City': 'Information about Oklahoma City',
        'Tulsa': 'Information about Tulsa',
        'Norman': 'Information about Norman',
    },
    'Oregon': {
        'Portland': 'Information about Portland',
        'Salem': 'Information about Salem',
        'Eugene': 'Information about Eugene',
    },
    'Pennsylvania': {
        'Philadelphia': 'Information about Philadelphia',
        'Pittsburgh': 'Information about Pittsburgh',
        'Allentown': 'Information about Allentown',
    },
    'Rhode Island': {
        'Providence': 'Information about Providence',
        'Warwick': 'Information about Warwick',
        'Cranston': 'Information about Cranston',
    },
    'South Carolina': {
        'Columbia': 'Information about Columbia',
        'Charleston': 'Information about Charleston',
        'North Charleston': 'Information about North Charleston',
    },
    'South Dakota': {
        'Sioux Falls': 'Information about Sioux Falls',
        'Rapid City': 'Information about Rapid City',
        'Aberdeen': 'Information about Aberdeen',
    },
    'Tennessee': {
        'Nashville': 'Information about Nashville',
        'Memphis': 'Information about Memphis',
        'Knoxville': 'Information about Knoxville',
    },
    'Texas': {
        'Houston': 'Information about Houston',
        'San Antonio': 'Information about San Antonio',
        'Dallas': 'Information about Dallas',
    },
    'Utah': {
        'Salt Lake City': 'Information about Salt Lake City',
        'West Valley City': 'Information about West Valley City',
        'Provo': 'Information about Provo',
    },
    'Vermont': {
        'Burlington': 'Information about Burlington',
        'Essex': 'Information about Essex',
        'South Burlington': 'Information about South Burlington',
    },
    'Virginia': {
        'Virginia Beach': 'Information about Virginia Beach',
        'Norfolk': 'Information about Norfolk',
        'Chesapeake': 'Information about Chesapeake',
    },
    'Washington': {
        'Seattle': 'Information about Seattle',
        'Spokane': 'Information about Spokane',
        'Tacoma': 'Information about Tacoma',
    },
    'West Virginia': {
        'Charleston': 'Information about Charleston',
        'Huntington': 'Information about Huntington',
        'Morgantown': 'Information about Morgantown',
    },
    'Wisconsin': {
        'Milwaukee': 'Information about Milwaukee',
        'Madison': 'Information about Madison',
        'Green Bay': 'Information about Green Bay',
    },
    'Wyoming': {
        'Cheyenne': 'Information about Cheyenne',
        'Casper': 'Information about Casper',
        'Laramie': 'Information about Laramie',
    }
}


state = selected_state.get()
print(state)

if state:  # Check if both state is non-empty
    # Get the city names based on the selected state
    city_names = city_info[state].keys()

    # create a combobox
    selected_city = tk.StringVar()

    ### search box for cities frame ###
    search_frame1 = tk.Frame(window, width=800, height=600, bg = "black", highlightbackground="white", highlightthickness=2)
    search_frame1.pack(padx=150, pady=100, anchor=tk.N, side="right")

    label2 = tk.Label(search_frame1, text="Please select a city:", font=("Comic Sans Serif",12), fg="white", wraplength=200, bg="black", anchor=tk.W)
    label2.pack(fill=tk.X)

    # drop down box
    city = ttk.Combobox(search_frame1, textvariable=selected_city)
    city['values'] = list(city_names)

    # place the widget
    city.pack(fill=tk.X, padx=5, pady=5)

    city.bind('<<ComboboxSelected>>', city_changed)

    city_value = selected_city.get()
    print(city_value)

    if city_value: # Check if city is non-empty
        text_info = city_info[state][city_value]
        print(text_info)
    else:
        print("Invalid city selected")

    # if state and city: # Check if both state and city are non-empty
    #     text_info = city_info[state][city]
    #     print(text_info)
else:
    print("Invalid state selected")

window.mainloop()
