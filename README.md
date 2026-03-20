# E-commerce Data Architecture & Polyglot Persistence

### 📌 Project Overview
This project involved designing a hybrid database system for a large-scale e-commerce marketplace (Olist Brazil). It demonstrates Polyglot Persistence—the strategic use of different database technologies to handle both structured transactions and unstructured customer feedback.

### 🛠️ Technical Implementation
Data Modeling: Created an ER Diagram and used DBDL to define relationships between customers, orders, and logistics.

Relational (SQL): Implemented Microsoft SQL Server to manage 100k+ structured transaction records, ensuring ACID compliance and data integrity.

NoSQL (MongoDB): Integrated MongoDB to store unstructured data, specifically customer reviews and flexible product metadata that does not fit a rigid schema.

Architecture: Developed a workflow to query across both systems, optimizing the database for both high-speed writes (orders) and analytical reads (reviews).

### 📊 Analytical Outcome
This project demonstrates the design and implementation of a scalable database architecture for an e-commerce platform using a combination of relational (RDBMS) and NoSQL databases. By applying polyglot persistence, the system effectively manages both structured and unstructured data, ensuring high performance, consistency, and flexibility. Overall, the solution enables efficient data handling, supports business analytics, and improves decision-making for real-world e-commerce operations.

### 🚀 Tech Stack
MS SQL Server | MongoDB | DBDL | SQL | JSON
