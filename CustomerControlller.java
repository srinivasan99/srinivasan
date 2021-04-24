package com.javainuse.controllers;

import java.util.List;


import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;


import com.javainuse.model.Customer;

@Controller
public class CustomerController {

	
	

	@RequestMapping(value = "/allCustomers.html", method = RequestMethod.POST)
	public String newCustomer(Customer customer) {

		CustomerData.save(customer);
		return ("redirect:/newCustomer.html");

	}

}
