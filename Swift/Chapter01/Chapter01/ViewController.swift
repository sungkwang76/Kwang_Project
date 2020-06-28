//
//  ViewController.swift
//  Chapter01
//
//  Created by sung kwang kim on 2020/01/26.
//  Copyright © 2020 sung kwang kim. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet var uiTitle: UILabel!
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }


    @IBAction func sayHello(_ sender: Any) {
        self.uiTitle.text = "Hello, World!"
    }
}

