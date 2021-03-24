This is a database that I created so that I could practice different database concepts.

Concepts include:  
		-Creating databases and tables  
		- Creating relationships between tables through Primary (and Foreign) Keys  
		- Editing tables (names, data types, etc.)  

I did most of the editing manually in the terminal, but sometimes, for more complex functions, I used MySQL Workbench.  

The database is made up of 3 tables:
* **Family**  
* **Siblings_c**  
* **Siblings-w**

**Family**: This table contains all of my relatives, ranging from my immmediate family to my parents' siblings and my grandparents.
There are 10 columns:
* firstname  
* middlename  
* lastname  
* age  
* sex  
* pat_mat: This is a yes or no answer signifying whether or not the person is a parent.  
* birthdate  
* **fam_id_c**: If they are on my father's side, this id will correspond to their nuclear family id (**order_num**) in the **Siblings_c** table.  
* **fam_id_w**: If they are on my mother's side, this id will correspond to their nuclear family id (**order_num**) in the **Siblings_w** table.  
* **pers_id**: This is the primary key and each person's unique identifier.  

**Siblings_c**: This table contains my father's siblings.
There are 3 columns:  
* firstname  
* order_num: This is the respective sibling's number in terms of order of birth. For example, the firstborn would be 1. Also, if the firstborn has a child, that child's **fam_id_c** value (in the Family table) would be 1 as well.
* **pers_id**: This is a Foreign key that links this table back to the Family table.

The **Siblings_w** table is the same as **Siblings_c** but with my mother's siblings.
