# IFCO

Project Structure
```
IFCO/
├──  data-engineering-test
    ├── resources/
        ├── invoicing_data.json
        ├── orders.csv
    ├── source
        ├── outputs/
        ├── test/
            ├── __init__.py
            ├── test_invoices.json
            ├── test_transformation_commission_salers/py
            ├── test_transformation_company_salers.py
            ├── test_transformation_invoices.py
            ├── test_transformation_orders_invoicing.py
            ├── test_transformation_orders.py
            ├── utils.py
            
        ├── transformations/
            ├── __init__.py
            ├── transform_commissions_salers.py
            ├── transform_company_salers.py
            ├── transform_invoicing.py
            ├── transform_orders_invoicing.py
            ├──transfor_orders.py
    ├── task_1.py
    ├── task_2.py
    ├── task_3.py
    ├── task_4.py
    ├── task_5.py
    ├── task_6.py
├── Dockerfile
├── README.md
├── requirements.txt
├── run-docker.sh
├── run_tests.sh
└── setup.py
```