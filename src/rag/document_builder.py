class DocumentBuilder:

    @staticmethod
    def build_order_documents(df):
        documents = []
        for _, row in df.iterrows():
            doc = (
                f"Order ID: {row['order_id']}. "
                f"Warehouse: {row['warehouse']}. "
                f"Region: {row['region']}. "
                f"Product: {row['product']}. "
                f"Quantity: {row['order_qty']}. "
                f"Delivery Time: {row['delivery_time_days']} days. "
                f"Status: {row['status']}."
            )
            documents.append(doc)
        return documents

    @staticmethod
    def build_inventory_documents(df):
        documents = []
        for _, row in df.iterrows():
            doc = (
                f"Inventory ID: {row['inventory_id']}. "
                f"Warehouse: {row['warehouse']}. "
                f"Product: {row['product']}. "
                f"Stock Level: {row['stock_level']}. "
                f"Reorder Level: {row['reorder_level']}. "
                f"Supplier: {row['supplier']}. "
                f"Transport Cost: {row['transport_cost']}."
            )
            documents.append(doc)
        return documents