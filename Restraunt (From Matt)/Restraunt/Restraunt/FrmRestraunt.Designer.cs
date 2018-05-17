namespace Restraunt
{
    partial class FrmRestraunt
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.GrpDrink = new System.Windows.Forms.GroupBox();
            this.RdoPop = new System.Windows.Forms.RadioButton();
            this.RdoWater = new System.Windows.Forms.RadioButton();
            this.GrpSide = new System.Windows.Forms.GroupBox();
            this.RdoSalad = new System.Windows.Forms.RadioButton();
            this.RdoSoup = new System.Windows.Forms.RadioButton();
            this.GrpEntree = new System.Windows.Forms.GroupBox();
            this.RdoSpaghetti = new System.Windows.Forms.RadioButton();
            this.RdoSteak = new System.Windows.Forms.RadioButton();
            this.BtnBill = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.LblTax = new System.Windows.Forms.Label();
            this.LblDrink = new System.Windows.Forms.Label();
            this.LblSide = new System.Windows.Forms.Label();
            this.LblEntree = new System.Windows.Forms.Label();
            this.LblBill = new System.Windows.Forms.Label();
            this.BtnClear = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.TxtName = new System.Windows.Forms.TextBox();
            this.GrpDrink.SuspendLayout();
            this.GrpSide.SuspendLayout();
            this.GrpEntree.SuspendLayout();
            this.SuspendLayout();
            // 
            // GrpDrink
            // 
            this.GrpDrink.Controls.Add(this.RdoPop);
            this.GrpDrink.Controls.Add(this.RdoWater);
            this.GrpDrink.Location = new System.Drawing.Point(24, 54);
            this.GrpDrink.Name = "GrpDrink";
            this.GrpDrink.Size = new System.Drawing.Size(200, 100);
            this.GrpDrink.TabIndex = 0;
            this.GrpDrink.TabStop = false;
            this.GrpDrink.Text = "Drink";
            // 
            // RdoPop
            // 
            this.RdoPop.AutoSize = true;
            this.RdoPop.Location = new System.Drawing.Point(16, 64);
            this.RdoPop.Name = "RdoPop";
            this.RdoPop.Size = new System.Drawing.Size(44, 17);
            this.RdoPop.TabIndex = 1;
            this.RdoPop.TabStop = true;
            this.RdoPop.Text = "Pop";
            this.RdoPop.UseVisualStyleBackColor = true;
            this.RdoPop.CheckedChanged += new System.EventHandler(this.RdoPop_CheckedChanged);
            // 
            // RdoWater
            // 
            this.RdoWater.AutoSize = true;
            this.RdoWater.Location = new System.Drawing.Point(16, 30);
            this.RdoWater.Name = "RdoWater";
            this.RdoWater.Size = new System.Drawing.Size(54, 17);
            this.RdoWater.TabIndex = 0;
            this.RdoWater.TabStop = true;
            this.RdoWater.Text = "Water";
            this.RdoWater.UseVisualStyleBackColor = true;
            this.RdoWater.CheckedChanged += new System.EventHandler(this.RdoWater_CheckedChanged);
            // 
            // GrpSide
            // 
            this.GrpSide.Controls.Add(this.RdoSalad);
            this.GrpSide.Controls.Add(this.RdoSoup);
            this.GrpSide.Location = new System.Drawing.Point(24, 193);
            this.GrpSide.Name = "GrpSide";
            this.GrpSide.Size = new System.Drawing.Size(200, 100);
            this.GrpSide.TabIndex = 1;
            this.GrpSide.TabStop = false;
            this.GrpSide.Text = "Side";
            // 
            // RdoSalad
            // 
            this.RdoSalad.AutoSize = true;
            this.RdoSalad.Location = new System.Drawing.Point(16, 54);
            this.RdoSalad.Name = "RdoSalad";
            this.RdoSalad.Size = new System.Drawing.Size(52, 17);
            this.RdoSalad.TabIndex = 1;
            this.RdoSalad.TabStop = true;
            this.RdoSalad.Text = "Salad";
            this.RdoSalad.UseVisualStyleBackColor = true;
            this.RdoSalad.CheckedChanged += new System.EventHandler(this.RdoSalad_CheckedChanged);
            // 
            // RdoSoup
            // 
            this.RdoSoup.AutoSize = true;
            this.RdoSoup.Location = new System.Drawing.Point(16, 20);
            this.RdoSoup.Name = "RdoSoup";
            this.RdoSoup.Size = new System.Drawing.Size(50, 17);
            this.RdoSoup.TabIndex = 0;
            this.RdoSoup.TabStop = true;
            this.RdoSoup.Text = "Soup";
            this.RdoSoup.UseVisualStyleBackColor = true;
            this.RdoSoup.CheckedChanged += new System.EventHandler(this.RdoSoup_CheckedChanged);
            // 
            // GrpEntree
            // 
            this.GrpEntree.Controls.Add(this.RdoSpaghetti);
            this.GrpEntree.Controls.Add(this.RdoSteak);
            this.GrpEntree.Location = new System.Drawing.Point(24, 332);
            this.GrpEntree.Name = "GrpEntree";
            this.GrpEntree.Size = new System.Drawing.Size(200, 100);
            this.GrpEntree.TabIndex = 2;
            this.GrpEntree.TabStop = false;
            this.GrpEntree.Text = "Entree";
            // 
            // RdoSpaghetti
            // 
            this.RdoSpaghetti.AutoSize = true;
            this.RdoSpaghetti.Location = new System.Drawing.Point(16, 63);
            this.RdoSpaghetti.Name = "RdoSpaghetti";
            this.RdoSpaghetti.Size = new System.Drawing.Size(70, 17);
            this.RdoSpaghetti.TabIndex = 1;
            this.RdoSpaghetti.TabStop = true;
            this.RdoSpaghetti.Text = "Spaghetti";
            this.RdoSpaghetti.UseVisualStyleBackColor = true;
            this.RdoSpaghetti.CheckedChanged += new System.EventHandler(this.RdoSpaghetti_CheckedChanged);
            // 
            // RdoSteak
            // 
            this.RdoSteak.AutoSize = true;
            this.RdoSteak.Location = new System.Drawing.Point(16, 30);
            this.RdoSteak.Name = "RdoSteak";
            this.RdoSteak.Size = new System.Drawing.Size(53, 17);
            this.RdoSteak.TabIndex = 0;
            this.RdoSteak.TabStop = true;
            this.RdoSteak.Text = "Steak";
            this.RdoSteak.UseVisualStyleBackColor = true;
            this.RdoSteak.CheckedChanged += new System.EventHandler(this.RdoSteak_CheckedChanged);
            // 
            // BtnBill
            // 
            this.BtnBill.Location = new System.Drawing.Point(364, 395);
            this.BtnBill.Name = "BtnBill";
            this.BtnBill.Size = new System.Drawing.Size(112, 37);
            this.BtnBill.TabIndex = 3;
            this.BtnBill.Text = "Calculate Total Bill";
            this.BtnBill.UseVisualStyleBackColor = true;
            this.BtnBill.Click += new System.EventHandler(this.BtnBill_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(399, 362);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(38, 16);
            this.label1.TabIndex = 4;
            this.label1.Text = "Tax:";
            // 
            // LblTax
            // 
            this.LblTax.AutoSize = true;
            this.LblTax.Location = new System.Drawing.Point(443, 366);
            this.LblTax.Name = "LblTax";
            this.LblTax.Size = new System.Drawing.Size(19, 13);
            this.LblTax.TabIndex = 5;
            this.LblTax.Text = "$0";
            // 
            // LblDrink
            // 
            this.LblDrink.AutoSize = true;
            this.LblDrink.Location = new System.Drawing.Point(231, 84);
            this.LblDrink.Name = "LblDrink";
            this.LblDrink.Size = new System.Drawing.Size(19, 13);
            this.LblDrink.TabIndex = 6;
            this.LblDrink.Text = "$0";
            // 
            // LblSide
            // 
            this.LblSide.AutoSize = true;
            this.LblSide.Location = new System.Drawing.Point(231, 213);
            this.LblSide.Name = "LblSide";
            this.LblSide.Size = new System.Drawing.Size(19, 13);
            this.LblSide.TabIndex = 7;
            this.LblSide.Text = "$0";
            // 
            // LblEntree
            // 
            this.LblEntree.AutoSize = true;
            this.LblEntree.Location = new System.Drawing.Point(231, 362);
            this.LblEntree.Name = "LblEntree";
            this.LblEntree.Size = new System.Drawing.Size(19, 13);
            this.LblEntree.TabIndex = 8;
            this.LblEntree.Text = "$0";
            // 
            // LblBill
            // 
            this.LblBill.AutoSize = true;
            this.LblBill.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.LblBill.Location = new System.Drawing.Point(360, 435);
            this.LblBill.Name = "LblBill";
            this.LblBill.Size = new System.Drawing.Size(27, 20);
            this.LblBill.TabIndex = 9;
            this.LblBill.Text = "$0";
            // 
            // BtnClear
            // 
            this.BtnClear.Location = new System.Drawing.Point(535, 12);
            this.BtnClear.Name = "BtnClear";
            this.BtnClear.Size = new System.Drawing.Size(75, 23);
            this.BtnClear.TabIndex = 10;
            this.BtnClear.Text = "Clear";
            this.BtnClear.UseVisualStyleBackColor = true;
            this.BtnClear.Click += new System.EventHandler(this.BtnClear_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(361, 151);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(38, 13);
            this.label2.TabIndex = 11;
            this.label2.Text = "Name:";
            // 
            // TxtName
            // 
            this.TxtName.Location = new System.Drawing.Point(405, 148);
            this.TxtName.Name = "TxtName";
            this.TxtName.Size = new System.Drawing.Size(100, 20);
            this.TxtName.TabIndex = 12;
            // 
            // FrmRestraunt
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(622, 520);
            this.Controls.Add(this.TxtName);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.BtnClear);
            this.Controls.Add(this.LblBill);
            this.Controls.Add(this.LblEntree);
            this.Controls.Add(this.LblSide);
            this.Controls.Add(this.LblDrink);
            this.Controls.Add(this.LblTax);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.BtnBill);
            this.Controls.Add(this.GrpEntree);
            this.Controls.Add(this.GrpSide);
            this.Controls.Add(this.GrpDrink);
            this.Name = "FrmRestraunt";
            this.Text = "Restraunt";
            this.Load += new System.EventHandler(this.FrmRestraunt_Load);
            this.GrpDrink.ResumeLayout(false);
            this.GrpDrink.PerformLayout();
            this.GrpSide.ResumeLayout(false);
            this.GrpSide.PerformLayout();
            this.GrpEntree.ResumeLayout(false);
            this.GrpEntree.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.GroupBox GrpDrink;
        private System.Windows.Forms.RadioButton RdoPop;
        private System.Windows.Forms.RadioButton RdoWater;
        private System.Windows.Forms.GroupBox GrpSide;
        private System.Windows.Forms.GroupBox GrpEntree;
        private System.Windows.Forms.RadioButton RdoSalad;
        private System.Windows.Forms.RadioButton RdoSoup;
        private System.Windows.Forms.RadioButton RdoSpaghetti;
        private System.Windows.Forms.RadioButton RdoSteak;
        private System.Windows.Forms.Button BtnBill;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label LblTax;
        private System.Windows.Forms.Label LblDrink;
        private System.Windows.Forms.Label LblSide;
        private System.Windows.Forms.Label LblEntree;
        private System.Windows.Forms.Label LblBill;
        private System.Windows.Forms.Button BtnClear;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox TxtName;
    }
}

