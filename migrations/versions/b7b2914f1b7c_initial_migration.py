"""initial migration

Revision ID: b7b2914f1b7c
Revises: 
Create Date: 2024-08-27 11:33:25.105301

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b7b2914f1b7c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('slug', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('slug')
    )
    op.drop_table('product')
    op.drop_table('_prisma_migrations')
    op.drop_table('sales_item')
    op.drop_table('sales_person')
    with op.batch_alter_table('transaction', schema=None) as batch_op:
        batch_op.drop_index('transaction_id')
        batch_op.drop_index('transaction_id_2')

    op.drop_table('transaction')
    op.drop_table('customer')
    op.drop_table('sales_order')
    op.drop_table('item')
    op.drop_table('product_type')
    op.drop_table('type')
    with op.batch_alter_table('cart_items', schema=None) as batch_op:
        batch_op.alter_column('quantity',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('unit_price',
               existing_type=sa.NUMERIC(precision=20, scale=4),
               type_=sa.Float(),
               nullable=True,
               existing_server_default=sa.text('0.00'))
        batch_op.alter_column('total_price',
               existing_type=sa.NUMERIC(precision=20, scale=4),
               type_=sa.Float(),
               nullable=True,
               existing_server_default=sa.text('0.00'))
        batch_op.alter_column('carts_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('products_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.drop_constraint('uk_cart_items', type_='unique')
        batch_op.create_foreign_key(None, 'product', ['products_id'], ['id'])

    with op.batch_alter_table('carts', schema=None) as batch_op:
        batch_op.alter_column('total_price',
               existing_type=sa.NUMERIC(precision=20, scale=4),
               type_=sa.Float(),
               nullable=True,
               existing_server_default=sa.text('0.00'))
        batch_op.alter_column('date_created',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=True,
               existing_server_default=sa.text('now()'))
        batch_op.alter_column('date_modified',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=True,
               existing_server_default=sa.text('now()'))
        batch_op.alter_column('users_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    with op.batch_alter_table('order_items', schema=None) as batch_op:
        batch_op.alter_column('product_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('orders_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('start_date',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               type_=sa.Date(),
               nullable=True)
        batch_op.alter_column('end_date',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               type_=sa.Date(),
               existing_nullable=True)
        batch_op.alter_column('status',
               existing_type=sa.VARCHAR(length=40),
               nullable=True)
        batch_op.alter_column('price',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=True)
        batch_op.alter_column('quantity',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('total_price',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=True)
        batch_op.create_foreign_key(None, 'product', ['product_id'], ['id'])

    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.alter_column('date_created',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               type_=sa.Date(),
               nullable=True,
               existing_server_default=sa.text('now()'))
        batch_op.alter_column('status',
               existing_type=sa.VARCHAR(length=40),
               nullable=True)
        batch_op.alter_column('total_price',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=True)
        batch_op.alter_column('users_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('budget',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.drop_column('role')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role', postgresql.ENUM('INTERN', 'ENGINEER', 'ADMIN', name='Role'), server_default=sa.text('\'INTERN\'::"Role"'), autoincrement=False, nullable=False))
        batch_op.alter_column('budget',
               existing_type=sa.INTEGER(),
               nullable=True)

    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.alter_column('users_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('total_price',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=False)
        batch_op.alter_column('status',
               existing_type=sa.VARCHAR(length=40),
               nullable=False)
        batch_op.alter_column('date_created',
               existing_type=sa.Date(),
               type_=postgresql.TIMESTAMP(timezone=True),
               nullable=False,
               existing_server_default=sa.text('now()'))

    with op.batch_alter_table('order_items', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('total_price',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=False)
        batch_op.alter_column('quantity',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('price',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=False)
        batch_op.alter_column('status',
               existing_type=sa.VARCHAR(length=40),
               nullable=False)
        batch_op.alter_column('end_date',
               existing_type=sa.Date(),
               type_=postgresql.TIMESTAMP(timezone=True),
               existing_nullable=True)
        batch_op.alter_column('start_date',
               existing_type=sa.Date(),
               type_=postgresql.TIMESTAMP(timezone=True),
               nullable=False)
        batch_op.alter_column('orders_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('product_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    with op.batch_alter_table('carts', schema=None) as batch_op:
        batch_op.alter_column('users_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('date_modified',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=False,
               existing_server_default=sa.text('now()'))
        batch_op.alter_column('date_created',
               existing_type=postgresql.TIMESTAMP(timezone=True),
               nullable=False,
               existing_server_default=sa.text('now()'))
        batch_op.alter_column('total_price',
               existing_type=sa.Float(),
               type_=sa.NUMERIC(precision=20, scale=4),
               nullable=False,
               existing_server_default=sa.text('0.00'))

    with op.batch_alter_table('cart_items', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_unique_constraint('uk_cart_items', ['carts_id', 'products_id'])
        batch_op.alter_column('products_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('carts_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('total_price',
               existing_type=sa.Float(),
               type_=sa.NUMERIC(precision=20, scale=4),
               nullable=False,
               existing_server_default=sa.text('0.00'))
        batch_op.alter_column('unit_price',
               existing_type=sa.Float(),
               type_=sa.NUMERIC(precision=20, scale=4),
               nullable=False,
               existing_server_default=sa.text('0.00'))
        batch_op.alter_column('quantity',
               existing_type=sa.INTEGER(),
               nullable=False)

    op.create_table('type',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('type_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('type_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='type_pk'),
    postgresql_ignore_search_path=False
    )
    op.create_table('product_type',
    sa.Column('type_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], name='fk_product_type_product_id_product_id'),
    sa.ForeignKeyConstraint(['type_id'], ['type.id'], name='fk_product_type_type_id_type_id'),
    sa.PrimaryKeyConstraint('type_id', 'product_id', name='product_type_pk')
    )
    op.create_table('item',
    sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('size', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('color', sa.VARCHAR(length=30), autoincrement=False, nullable=False),
    sa.Column('picture', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    sa.Column('price', sa.NUMERIC(precision=6, scale=2), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('item_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], name='item_product_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='item_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('sales_order',
    sa.Column('cust_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('sales_person_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('time_order_taken', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('purchase_order_number', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('credit_card_number', sa.VARCHAR(length=16), autoincrement=False, nullable=False),
    sa.Column('credit_card_exper_month', sa.SMALLINT(), autoincrement=False, nullable=False),
    sa.Column('credit_card_exper_day', sa.SMALLINT(), autoincrement=False, nullable=False),
    sa.Column('credit_card_secret_code', sa.SMALLINT(), autoincrement=False, nullable=False),
    sa.Column('name_on_card', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('sales_order_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['cust_id'], ['customer.id'], name='sales_order_cust_id_fkey'),
    sa.ForeignKeyConstraint(['sales_person_id'], ['sales_person.id'], name='sales_order_sales_person_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='sales_order_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('customer',
    sa.Column('first_name', sa.VARCHAR(length=30), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=30), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=60), autoincrement=False, nullable=False),
    sa.Column('company', sa.VARCHAR(length=60), autoincrement=False, nullable=True),
    sa.Column('street', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('city', sa.VARCHAR(length=40), autoincrement=False, nullable=False),
    sa.Column('state', sa.CHAR(length=2), server_default=sa.text("'PA'::bpchar"), autoincrement=False, nullable=False),
    sa.Column('zip', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('phone', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('birth_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('sex', postgresql.ENUM('M', 'F', name='sex_type'), autoincrement=False, nullable=False),
    sa.Column('date_entered', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('customer_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='customer_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('transaction',
    sa.Column('name', sa.VARCHAR(length=30), autoincrement=False, nullable=False),
    sa.Column('payment_type', sa.VARCHAR(length=30), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='transaction_type_pkey')
    )
    with op.batch_alter_table('transaction', schema=None) as batch_op:
        batch_op.create_index('transaction_id_2', ['name', 'payment_type'], unique=False)
        batch_op.create_index('transaction_id', ['name'], unique=False)

    op.create_table('sales_person',
    sa.Column('first_name', sa.VARCHAR(length=30), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=30), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=60), autoincrement=False, nullable=False),
    sa.Column('street', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('city', sa.VARCHAR(length=40), autoincrement=False, nullable=False),
    sa.Column('state', sa.CHAR(length=2), server_default=sa.text("'PA'::bpchar"), autoincrement=False, nullable=False),
    sa.Column('zip', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('phone', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('birth_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('sex', postgresql.ENUM('M', 'F', name='sex_type'), autoincrement=False, nullable=False),
    sa.Column('date_hired', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('sales_person_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='sales_person_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('sales_item',
    sa.Column('item_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('sales_order_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('quantity', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('discount', sa.NUMERIC(precision=3, scale=2), server_default=sa.text('0'), autoincrement=False, nullable=True),
    sa.Column('taxable', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=False),
    sa.Column('sales_tax_rate', sa.NUMERIC(precision=5, scale=2), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], name='sales_item_item_id_fkey'),
    sa.ForeignKeyConstraint(['sales_order_id'], ['sales_order.id'], name='sales_item_sales_order_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='sales_item_pkey')
    )
    op.create_table('_prisma_migrations',
    sa.Column('id', sa.VARCHAR(length=36), autoincrement=False, nullable=False),
    sa.Column('checksum', sa.VARCHAR(length=64), autoincrement=False, nullable=False),
    sa.Column('finished_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('migration_name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('logs', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('rolled_back_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('started_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=False),
    sa.Column('applied_steps_count', sa.INTEGER(), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='_prisma_migrations_pkey')
    )
    op.create_table('product',
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('supplier', sa.VARCHAR(length=30), autoincrement=False, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('price', sa.NUMERIC(precision=6, scale=2), autoincrement=False, nullable=True),
    sa.Column('sku', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='product_pkey')
    )
    op.drop_table('category')
    # ### end Alembic commands ###
