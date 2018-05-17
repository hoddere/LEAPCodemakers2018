using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace Restraunt
{
    public partial class FrmRestraunt : Form
    {
        public FrmRestraunt()
        {
            InitializeComponent();
        }
        //these are all the variables used in the program
        double water, pop, steak, spaghetti, soup, salad;
        double tax, cost, entree, side, drink;

    private void FrmRestraunt_Load(object sender, EventArgs e)
        {
        //holds the value for how much each item costs
            water = 1;
            pop = 2;
            salad = 4;
            soup = 5;
            steak = 15.50;
            spaghetti = 10.50;

        }

        private void RdoWater_CheckedChanged(object sender, EventArgs e)
        {
            LblDrink.Text = water.ToString("c");//shows price of water when it's check off
            drink = water;//sets the drink value to the price of water
        }

        private void RdoPop_CheckedChanged(object sender, EventArgs e)
        {
            LblDrink.Text = pop.ToString("c");//shows price of pop when it's check off
            drink = pop;//sets the drink value to the price of pop
        }

        private void RdoSoup_CheckedChanged(object sender, EventArgs e)
        {
            LblSide.Text = soup.ToString("c");//shows price of soup when it's check off
            side = soup;//sets the side value to the price of soup
        }

        private void RdoSalad_CheckedChanged(object sender, EventArgs e)
        {
            LblSide.Text = salad.ToString("c");//shows price of salad when it's check off
            side = salad;//sets the side value to the price of salad
        }

        private void RdoSteak_CheckedChanged(object sender, EventArgs e)
        {
            LblEntree.Text = steak.ToString("c");//shows price of steak when it's check off
            entree = steak;//sets the entree value to the price of steak 
        }

        private void RdoSpaghetti_CheckedChanged(object sender, EventArgs e)
        {
            LblEntree.Text = spaghetti.ToString("c");//shows price of spaghetti when it's check off
            entree = spaghetti; //sets the entree value to the price of spaghetti
        }

        private void BtnClear_Click(object sender, EventArgs e)
        {
            //restets everything so the user can start again
            RdoWater.Checked = false;//unchecks all the radio buttons
            RdoPop.Checked = false;
            RdoSalad.Checked = false;
            RdoSoup.Checked = false;
            RdoSteak.Checked = false;
            RdoSpaghetti.Checked = false;

            //resets all the visual amounts to $0
            LblDrink.Text = "$0";
            LblSide.Text = "$0";
            LblEntree.Text = "$0";
            LblTax.Text = "$0";
            LblBill.Text = "$0";

            //actually resets the values to $0
            drink = 0;
            entree = 0;
            side = 0;
            tax = 0;
            cost = 0;

        }

        private void BtnBill_Click(object sender, EventArgs e)
        {
            tax = (drink + side + entree) * 0.13;//calculates the tax of the meal
            LblTax.Text = tax.ToString("c");//shows user how much the take is

            cost = (drink + side + entree) * 1.13;//adds up cost of the meal and adds tax as well
            LblBill.Text = cost.ToString("c");//displays the total cost of th emeal to the user
        }




    }
}
