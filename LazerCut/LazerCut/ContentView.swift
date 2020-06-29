//
//  ContentView.swift
//  LazerCut
//
//  Created by Anthony Silva on 6/29/20.
//  Copyright © 2020 Anthony Silva. All rights reserved.
//

import SwiftUI

struct ContentView: View {
       @State var MachineXstring = ""
       @State var MachineYstring = ""
       @State var MachineX = Int.self
       @State var MachineY = Int.self
       @State private var selection: Int? = nil
    var body: some View {
        
        NavigationView{

            ZStack{
        NavigationLink(destination: MachineMenu(), tag: 1, selection: self.$selection)
                                              
                   {
                   Text("")
                   }
            //Form that allows us to Take user input
               Form{
                Text("Machine Specs").font(.largeTitle).foregroundColor(.white)
                   Section{
                       TextField("Please enter in the machine's X Dimentions:", text: $MachineXstring).keyboardType(.decimalPad)
                   
                       TextField("Please enter in the machine's Y Dimentions", text:  $MachineYstring).keyboardType(.decimalPad)
                       }
                //Button that allows us to change Pages
    Button(action: {self.selection = 1} ){
    Text("Continue")
                }
               }

               }
   
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
