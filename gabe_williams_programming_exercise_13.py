import sqlite3
import random
import matplotlib.pyplot as plt

#set up the initial population database with 2025 data
def setup_population_db():
    try:
        #connect to the database (creates it if it doesn't exist)
        #erase old table start from scratch
        conn = sqlite3.connect('population_GW.db')
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS population")

        #make a table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS population (
                city TEXT NOT NULL,
                year INTEGER NOT NULL,
                population INTEGER NOT NULL
            )
        ''')

        #define the data for the 10 Florida cities
        florida_data = [
            ('Jacksonville', 2025, 985843),
            ('Miami', 2025, 455924),
            ('Tampa', 2025, 403362),
            ('Orlando', 2025, 320901),
            ('St. Petersburg', 2025, 261907),
            ('Hialeah', 2025, 221300),
            ('Port St. Lucie', 2025, 217523),
            ('Cape Coral', 2025, 204310),
            ('Tallahassee', 2025, 201255),
            ('Fort Lauderdale', 2025, 184592)
        ]

        #insert the data
        cursor.executemany(
            "INSERT INTO population (city, year, population) VALUES (?, ?, ?)",
            florida_data
        )

        #commit the changes and close
        conn.commit()
        print(f"Successfully created table and added {len(florida_data)} cities.")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        if conn:
            conn.close()

#print the population table (for debugging)
def read_population_data():
    try:
        #connect to the database file
        conn = sqlite3.connect('population_GW.db')

        #create a cursor object to execute SQL
        cursor = conn.cursor()

        #query the system table for all entries of the table type
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

        tables = cursor.fetchall()

        if tables:
            print("Tables in the database:")
            for table in tables:
                print(f"- {table[0]}")
        else:
            print("No tables found in the database.")

        #use the select query
        cursor.execute("SELECT city, year, population FROM population ORDER BY city ASC, year ASC")

        #gather all the results
        rows = cursor.fetchall()

        #print the results
        print(f"{'City':<20} | {'Year':<6} | {'Population':<12}")
        print("-" * 42)

        for row in rows:
            # row[0] = city, row[1] = year, row[2] = population
            print(f"{row[0]:<20} | {row[1]:<6} | {row[2]:<12,}")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        if conn:
            conn.close()


#uses random growth rates for 20 years
def extend_population_to_2045():
    db_path = 'population_GW.db'

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        #gets current population numbers
        cursor.execute("SELECT city, year, population FROM population WHERE year = 2025")
        current_data = cursor.fetchall()

        if not current_data:
            print("No data found for the year 2025 to project from.")
            return

        projected_records = []

        #goes through each city to calculate its growth until 2045
        for city, start_year, start_pop in current_data:
            running_population = start_pop

            for year in range(start_year + 1, 2046):
                #picks a random growth rate between -2% and +8%
                growth_rate = random.uniform(-0.02, 0.08)

                #calculates the new population and rounds to nearest whole number
                running_population = int(running_population * (1 + growth_rate))

                #append to the list of records
                projected_records.append((city, year, max(0, running_population)))

        #inserts the new fabricated data into the table
        cursor.executemany(
            "INSERT INTO population (city, year, population) VALUES (?, ?, ?)",
            projected_records
        )

        conn.commit()
        print(f"Successfully added {len(projected_records)} projection records through 2045.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()


# Print all the cities to pick from
def print_city_list():
    try:
        #connects to the database
        conn = sqlite3.connect('population_GW.db')
        cursor = conn.cursor()

        #uses DISTINCT to get a unique list of cities
        cursor.execute("SELECT DISTINCT city FROM population ORDER BY city ASC")

        cities = cursor.fetchall()

        if cities:
            print(f"Cities in Florida::")
            print("-" * 30)
            for city in cities:
                print(f"• {city[0]}")
        else:
            print("No cities found in the population table.")

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

#plots data for a city using matplotlib
def plot_city_population(city_name):
    try:
        #connects to the database
        conn = sqlite3.connect('population_GW.db')
        cursor = conn.cursor()

        #fetches year and population for the specific city
        cursor.execute("""
            SELECT year, population 
            FROM population 
            WHERE city = ? 
            ORDER BY year
        """, (city_name,))

        data = cursor.fetchall()

        if not data:
            print(f"No data found for city: {city_name}")
            return

        #prepares data for plotting
        years = [row[0] for row in data]
        populations = [row[1] for row in data]

        #creates the plot
        plt.figure(figsize=(10, 6))
        plt.plot(years, populations, marker='o', linestyle='-', color='teal', linewidth=2)

        #adds titles and labels
        plt.title(f"Population Trends/Projections for {city_name}", fontsize=14)
        plt.xlabel("Year", fontsize=12)
        plt.ylabel("Population", fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)

        #formatting y-axis to show full numbers with commas separating them
        plt.ticklabel_format(style='plain', axis='y')

        #shows the plot
        plt.savefig(f"{city_name.replace(' ', '_')}_growth.png")
        print(f"Graph generated: {city_name.replace(' ', '_')}_growth.png")
        plt.show()

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

def user_interface():
    print_city_list()
    city = input("Enter a city name: ")
    plot_city_population(city)

setup_population_db()
extend_population_to_2045()
user_interface()