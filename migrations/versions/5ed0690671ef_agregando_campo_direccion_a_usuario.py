"""Agregando campo 'direccion' a Usuario

Revision ID: 5ed0690671ef
Revises: 
Create Date: 2023-09-03 17:05:04.936422

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5ed0690671ef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('agenda')
    op.drop_table('usuario')
    op.drop_table('diagnostico')
    op.drop_table('cita')
    op.drop_table('venta')
    op.drop_table('sede')
    op.drop_table('personalizacion')
    op.drop_table('producto_almacenad')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('producto_almacenad',
    sa.Column('id_Pr', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=True, nullable=False),
    sa.Column('tipo', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('lente', mysql.VARCHAR(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id_Pr'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('personalizacion',
    sa.Column('id_p', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=True, nullable=False),
    sa.Column('color', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('tipo', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('lente', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('urlfo', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('id_u', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id_u'], ['usuario.id_u'], name='personalizacion_ibfk_1'),
    sa.PrimaryKeyConstraint('id_p'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('sede',
    sa.Column('id_s', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=True, nullable=False),
    sa.Column('direccion', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('n_trabajadores', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('telefono', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id_s'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('venta',
    sa.Column('id_p', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=True, nullable=False),
    sa.Column('valor', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('descripcion_cosas', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('id_per', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=False, nullable=False),
    sa.Column('id_pr', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id_per'], ['personalizacion.id_p'], name='venta_ibfk_1'),
    sa.ForeignKeyConstraint(['id_pr'], ['producto_almacenad.id_Pr'], name='venta_ibfk_2'),
    sa.PrimaryKeyConstraint('id_p'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('cita',
    sa.Column('id_c', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=True, nullable=False),
    sa.Column('fecha_hora', mysql.DATETIME(), nullable=False),
    sa.Column('id_us', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=False, nullable=False),
    sa.Column('id_s', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=False, nullable=False),
    sa.Column('id_a', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id_a'], ['agenda.id_a'], name='cita_ibfk_3'),
    sa.ForeignKeyConstraint(['id_s'], ['sede.id_s'], name='cita_ibfk_2'),
    sa.ForeignKeyConstraint(['id_us'], ['usuario.id_u'], name='cita_ibfk_1'),
    sa.PrimaryKeyConstraint('id_c'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('diagnostico',
    sa.Column('id_d', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=True, nullable=False),
    sa.Column('descripcion', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('enfermedad', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('id_u', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id_u'], ['usuario.id_u'], name='diagnostico_ibfk_1'),
    sa.PrimaryKeyConstraint('id_d'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('usuario',
    sa.Column('id_u', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=True, nullable=False),
    sa.Column('nombre', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('apellidos', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('edad', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=False, nullable=False),
    sa.Column('tel', mysql.BIGINT(display_width=20, unsigned=True), autoincrement=False, nullable=False),
    sa.Column('n_documento', mysql.BIGINT(display_width=20, unsigned=True), autoincrement=False, nullable=False),
    sa.Column('t_Documento', mysql.ENUM('RC', 'CC', 'TI'), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('dirrecion', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('rol', mysql.ENUM('doctor', 'pac', 'admin'), server_default=sa.text("'pac'"), nullable=True),
    sa.Column('contra', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('estado_u', mysql.ENUM('activo', 'no activo'), server_default=sa.text("'activo'"), nullable=True),
    sa.PrimaryKeyConstraint('id_u'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('agenda',
    sa.Column('id_a', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=True, nullable=False),
    sa.Column('fecha_hora_inicial', mysql.DATETIME(), nullable=False),
    sa.Column('fecha_hora_final', mysql.DATETIME(), nullable=False),
    sa.Column('id_doctor', mysql.INTEGER(display_width=10, unsigned=True), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id_doctor'], ['usuario.id_u'], name='agenda_ibfk_1'),
    sa.PrimaryKeyConstraint('id_a'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
