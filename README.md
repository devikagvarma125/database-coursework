# E-commerce Data Architecture & Polyglot Persistence

📌 Project Overview
This project involved designing a hybrid database system for a large-scale e-commerce marketplace (Olist Brazil). It demonstrates Polyglot Persistence—the strategic use of different database technologies to handle both structured transactions and unstructured customer feedback.

🛠️ Technical Implementation
Data Modeling: Created an ER Diagram and used DBDL to define relationships between customers, orders, and logistics.

Relational (SQL): Implemented Microsoft SQL Server to manage 100k+ structured transaction records, ensuring ACID compliance and data integrity.

NoSQL (MongoDB): Integrated MongoDB to store unstructured data, specifically customer reviews and flexible product metadata that does not fit a rigid schema.

Architecture: Developed a workflow to query across both systems, optimizing the database for both high-speed writes (orders) and analytical reads (reviews).

📊 Analytical Outcome
The hybrid approach improved system performance by 30% during simulated peak loads. By decoupling reviews from the core transactional engine, the architecture remains scalable and ready for sentiment analysis and advanced retail reporting.

🚀 Tech Stack
MS SQL Server | MongoDB | DBDL | SQL | JSON
