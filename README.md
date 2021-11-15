# E-commerce-back-end
# INTRODUCTION
This project explores the back-end of a rudimentary e-commerce marketplace. It aims to demonstrate the functionality that might be expected from such a platform. It is written in Python and implements a MySQL connection for managing database operations. 
1.The project may be conceptualized as follows:
  1.	Admins- These users are responsible for the upkeep of the platform. They have the ability to add more admins and increase the balance of a customer.
  2.	Vendors-They represent the selling side of the marketplace. They are allotted orders to deliver. They are also given a list of their orders, products and balance and can             keep track of them. 
  3.	Customers-They represent the buying side of the platform. They can purchase with an account balance and can browse items in the market place.
2.To support this functionality there are two more tables
  1.	Products- This table represents available products in the marketplace. It can be searched.
  2.	Orders-This table represents the pending orders in the marketplace.
3.Salient features:
  1.	Search function: This project implements fuzzy search and can adjust for errors in search keywords. This is a huge benefit to the consumers who are shown the top results. Also this prevents the entire product database being exposed which adds security.
  2.	Referential integrity-Primary and foreign keys are judiciously used throughout the project to maintain referential integrity

